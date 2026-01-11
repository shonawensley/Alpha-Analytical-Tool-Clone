# Master Validation Run Report — Connecticut4 — results 2026-01-07 (history workbook ~ 2026-01-06)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-07/Connecticut4/`
- Winners lens: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2026-01-07/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2026-01-07/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2026-01-07/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2026-01-07/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2026-01-07/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2026-01-07/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac4_winner_553_20260110_033411.html`
- `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_156_20260110_033410.html`

Winners JSON files:
- `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac4_winner_553_20260110_033411.json`
- `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/Connecticut4_vtrac6_winner_156_20260110_033410.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-07/Connecticut4/winners/Connecticut4/digest.md`.
- Q2: Stable environment quick read: Midday 156 (canon 156): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 553 (canon 355): exact_boxed=True exact_straight=True | rank 5461/5561 (rank_frac 0.982)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 553 idx4 (rank 18/35, frac 0.514), 156 idx6 (rank 27/35, frac 0.771)
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

### 2.Stable — Connecticut4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2026-01-07)

## Midday winner 156 (canonical 156)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=20 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 14 | rank 991/1396 (rank_frac 0.7098853868194842) | score 12.0 (top 38.5, ratio 0.3116883116883117, delta 26.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=3
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 553 (canonical 355)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=21 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 5461/5561 (rank_frac 0.9820176227297248) | score 7.0 (top 39.5, ratio 0.17721518987341772, delta 32.5) | section Midday, Set Set1, Draw Draw3, Col 5, hot 0, vt_straight 0.0 | why straight|cov1|double_mirror
- Compound (patterns_compound.csv): rank 1607/1755 (rank_frac 0.9156695156695157) | score 8.0 (top 112.0, ratio 0.07142857142857142, delta 104.0) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1|dblmirrorx1
- Families (patterns_families.csv): count 17 | rank 727/1396 (rank_frac 0.5207736389684814) | score 15.0 (top 38.5, ratio 0.38961038961038963, delta 23.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=10

## Top compound candidates (patterns_compound.csv)
- rank    4 | canon 224 | section Evening | score 91.0 | col1_hits 7 | hot2 11
- rank    7 | canon 229 | section Evening | score 82.5 | col1_hits 7 | hot2 11
- rank   12 | canon 228 | section Evening | score 77.5 | col1_hits 7 | hot2 11
- rank   13 | canon 2249 | section Evening | score 76.0 | col1_hits 7 | hot2 11
- rank   20 | canon 2289 | section Evening | score 66.0 | col1_hits 6 | hot2 11
- rank   22 | canon 2248 | section Evening | score 65.0 | col1_hits 7 | hot2 11
- rank   10 | canon 2249 | section Combined | score 80.0 | col1_hits 7 | hot2 11
- rank   19 | canon 289 | section Evening | score 69.0 | col1_hits 6 | hot2 11
- rank    6 | canon 229 | section Combined | score 83.0 | col1_hits 7 | hot2 11
- rank    3 | canon 2244 | section Combined | score 102.0 | col1_hits 9 | hot2 11

## Top families (patterns_families.csv)
- rank 1391 | family 35 | score 4.0 | hot2 0 | section Midday
- rank  285 | family 34 | score 22.0 | hot2 1 | section Midday
- rank  500 | family 25 | score 18.0 | hot2 1 | section Midday
- rank  224 | family 24 | score 23.5 | hot2 6 | section Midday
- rank  252 | family 25 | score 23.0 | hot2 2 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 156 (canon 156): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A); Evening 553 (canon 355): exact_boxed=True exact_straight=True | rank 5461/5561 (rank_frac 0.982)
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

### 2.Digit Reduction — Connecticut4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20260110)

## Midday winner 156 (canonical 156)
- Stamp (winner_stamp.json): items_total=84 | exact_any=0 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=84 | exact_any=0 vtrac_any=84 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=84 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 553 (canonical 355)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 156 (canonical 156)
- Stamp (winner_stamp.json): items_total=120 | exact_any=0 exact_final=0 | vtrac_any=120 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=120 | exact_any=0 vtrac_any=120 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=120 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=19.927143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 4 | pattern 224 | score_v2 19.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 5 | pattern 224 | score_v2 19.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 4 | pattern 224 | score_v2 19.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 5 | pattern 224 | score_v2 19.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 3 | pattern 224 | score_v2 19.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 224 | score_v2 19.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 2 | pattern 224 | score_v2 19.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 922 | score_v2 18.737143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 922 | score_v2 18.637143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 922 | score_v2 18.637143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 19.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 922 | score_v2 18.737143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 224 | score_v2 17.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 992 | score_v2 16.115714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 224 | score_v2 15.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 922 | score_v2 14.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 448 | score_v2 14.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 922 | score_v2 13.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 224 | score_v2 13.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 922 | score_v2 13.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 156 (canon 156): items_total=84 exact_any=0 vtrac_any=84 | top winner_present=False best_rank=None/22; Evening 553 (canon 355): items_total=12 exact_any=0 vtrac_any=12 | top winner_present=False best_rank=None/16; Combined 156 (canon 156): items_total=120 exact_any=0 vtrac_any=120 | top winner_present=False best_rank=None/14
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 224, 922, 224, 992, 224.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — Connecticut4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20260110_033911)

## Top indices (from enhanced JSON)
- index 30 | score 93.82306999999996 | features: presence=61.355569999999986, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 88.02561999999998 | features: presence=55.32811999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 28 | score 71.34129999999998 | features: presence=53.74379999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 61.19245999999999 | features: presence=45.21495999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 56.31879999999999 | features: presence=40.93129999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 32.113725 | features: presence=15.396225000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 11 | score 23.166605000000004 | features: presence=12.589105000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 33 | score 22.422850000000004 | features: presence=12.565350000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 10 | score 19.14078 | features: presence=10.29328, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 26 | score 11.166425 | features: presence=5.120799999999999, cross_section=0.5, set_echo=0.3, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
284, 487, 248, 824, 847, 784, 874, 347, 734, 324

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 553 | index 4 | file Connecticut4_vtrac4_winner_553_20260110_033411.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 156 | index 6 | file Connecticut4_vtrac6_winner_156_20260110_033410.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 553 | index 4 rank 18/35 (rank_frac 0.5142857142857142) | score 6.445058333333334 (top 93.82306999999996, ratio 0.06869374806572985, delta 87.37801166666662) | winner_in_index_straights=False | top_index_straights: (none)
- winner 156 | index 6 rank 27/35 (rank_frac 0.7714285714285715) | score 1.9772500000000002 (top 93.82306999999996, ratio 0.021074241122146196, delta 91.84581999999996) | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 553→idx4 rank 18/35 (frac 0.514); 156→idx6 rank 27/35 (frac 0.771).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 30, 27, 28, 31, 34.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — Connecticut4 — 2026-01-07

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2026-01-07)

## Midday winner 156 (canonical 156)
- Top lanes (hot_zones_top_lanes.csv): present | rank 206/210 (rank_frac 0.9809523809523809) | score_mean 13.175 (top 23.929, ratio 0.5505871536629195, delta 10.753999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 553 (canonical 355)
- Top lanes (hot_zones_top_lanes.csv): present | rank 114/210 (rank_frac 0.5428571428571428) | score_mean 16.994 (top 23.929, ratio 0.710184295206653, delta 6.934999999999999)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 066 | vt_triad 12 | score_mean 23.929 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 227 | vt_triad 33 | score_mean 21.819 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 113 | vt_triad 24 | score_mean 21.662 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 017 | vt_triad 123 | score_mean 21.635 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 277 | vt_triad 33 | score_mean 21.512 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 567 | vt_triad 123 | score_mean 21.468 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 278 | vt_triad 334 | score_mean 21.229 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 237 | vt_triad 334 | score_mean 21.108 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 668 | vt_triad 24 | score_mean 21.064 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 118 | vt_triad 24 | score_mean 21.007 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 156 (canon 156): rank 206/210 (rank_frac 0.981) ratio_to_top=0.5505871536629195; Evening 553 (canon 355): rank 114/210 (rank_frac 0.543) ratio_to_top=0.710184295206653
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

Aux draws snapshot dir: `sharepacks/2026-01-07/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2026-01-07

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-07/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-06.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=737, 576, 660, 071, 311
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=576, 071, 569, 533, 970
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-07/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=737, 660, 311, 181, 356

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=2 last_repeat_gap=43 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=24), P2:4 (gap=19), P3:4 (gap=32)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=36.27597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=36.220771428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=34.37056285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 494: score=34.31536285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 744: score=32.356028571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=32.30082857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 824: score=31.998 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 804: score=31.356164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 424: score=30.092591428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 884: score=29.6738 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=895 sev=B
- 129: ds=877 sev=B
- 288: ds=865 sev=B
- 149: ds=847 sev=B
- 445: ds=779 sev=B
- 114: ds=749 sev=B
- 069: ds=713 sev=B
- 888: ds=711 sev=B
- 688: ds=707 sev=B
- 133: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=97 sev=blue
  - 99: ds=78 sev=blue
  - 00: ds=48 sev=purple
  - 88: ds=34 sev=purple
  - 55: ds=16 sev=-
  - 22: ds=11 sev=-
  - 33: ds=7 sev=-
  - 11: ds=4 sev=-
  - 66: ds=2 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 48: ds=84 sev=red
  - 78: ds=80 sev=red
  - 49: ds=78 sev=red
  - 25: ds=47 sev=blue
  - 58: ds=29 sev=purple
  - 68: ds=29 sev=purple
  - 14: ds=27 sev=purple
  - 15: ds=27 sev=purple
  - 89: ds=24 sev=-
  - 34: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:413, 32:180, 25:166, 29:139, 4:137, 15:125, 31:114, 34:109, 3:94, 35:78

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=413 fs=1 fl=2 hz=0.01098901098901099, 32:ds=180 fs=5 fl=2 hz=0.011267605633802818, 25:ds=166 fs=22 fl=2 hz=0.029055690072639227, 29:ds=139 fs=24 fl=1 hz=0.03071253071253071, 4:ds=137 fs=21 fl=2 hz=0.027677496991576414, 15:ds=125 fs=9 fl=4 hz=0.015531660692951015, 31:ds=114 fs=32 fl=0 hz=0.03665521191294387, 34:ds=109 fs=15 fl=2 hz=0.01951779563719862, 3:ds=94 fs=27 fl=0 hz=0.030337078651685393, 35:ds=78 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=88 flags=purple
- S24: ds=80 flags=blue+purple
- S22: ds=78 flags=purple
- S25: ds=70 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=2 max=3 last_repeat_gap=1 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=31), P2:0 (gap=31), P3:4 (gap=35)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=36.27597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=36.220771428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=34.37056285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 494: score=34.31536285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 744: score=32.356028571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=32.30082857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 824: score=31.998 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 804: score=31.356164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 424: score=30.092591428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 884: score=29.6738 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=884 sev=B
- 478: ds=865 sev=B
- 459: ds=860 sev=B
- 159: ds=816 sev=B
- 099: ds=797 sev=B
- 127: ds=788 sev=B
- 559: ds=730 sev=B
- 004: ds=689 sev=B
- 155: ds=685 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=96 sev=blue
  - 88: ds=56 sev=purple
  - 44: ds=48 sev=purple
  - 55: ds=33 sev=purple
  - 00: ds=29 sev=purple
  - 66: ds=16 sev=-
  - 77: ds=11 sev=-
  - 11: ds=8 sev=-
  - 22: ds=5 sev=-
  - 33: ds=3 sev=-
- non_repeating:
  - 78: ds=74 sev=red
  - 13: ds=61 sev=red
  - 49: ds=48 sev=blue
  - 19: ds=47 sev=blue
  - 48: ds=44 sev=blue
  - 37: ds=28 sev=purple
  - 08: ds=26 sev=purple
  - 36: ds=24 sev=-
  - 25: ds=23 sev=-
  - 06: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:206, 25:107, 31:96, 32:94, 18:91, 3:79, 29:69, 4:68, 15:62, 34:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=206 fs=3 fl=0 hz=0.008565310492505354, 25:ds=107 fs=21 fl=1 hz=0.025974025974025976, 31:ds=96 fs=20 fl=2 hz=0.024608501118568233, 32:ds=94 fs=3 fl=4 hz=0.009510869565217392, 18:ds=91 fs=23 fl=1 hz=0.026519337016574582, 3:ds=79 fs=22 fl=2 hz=0.02631578947368421, 29:ds=69 fs=18 fl=2 hz=0.023446658851113716, 4:ds=68 fs=26 fl=0 hz=0.02931228861330327, 15:ds=62 fs=23 fl=1 hz=0.02564102564102564, 34:ds=54 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=90 flags=blue+purple
- S24: ds=87 flags=purple
- S23: ds=55 flags=purple

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
- current_index=27 streak=1 max=3 last_repeat_gap=3 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=21), P2:9 (gap=20), P3:2 (gap=18)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 844: score=36.27597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 894: score=36.220771428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 444: score=34.37056285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 494: score=34.31536285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 744: score=32.356028571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 794: score=32.30082857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 824: score=31.998 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 804: score=31.356164285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 424: score=30.092591428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 884: score=29.6738 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=911 sev=B
- 668: ds=908 sev=B
- 399: ds=907 sev=B
- 044: ds=903 sev=B
- 133: ds=900 sev=B
- 145: ds=872 sev=B
- 677: ds=779 sev=B
- 333: ds=774 sev=B
- 112: ds=726 sev=B
- 344: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=118 sev=red
  - 22: ds=75 sev=blue
  - 99: ds=39 sev=purple
  - 33: ds=25 sev=purple
  - 00: ds=24 sev=-
  - 88: ds=17 sev=-
  - 55: ds=8 sev=-
  - 11: ds=2 sev=-
  - 66: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 57: ds=54 sev=blue
  - 69: ds=52 sev=blue
  - 23: ds=49 sev=blue
  - 25: ds=47 sev=blue
  - 07: ds=46 sev=blue
  - 48: ds=42 sev=blue
  - 78: ds=40 sev=blue
  - 49: ds=39 sev=blue
  - 15: ds=32 sev=purple
  - 02: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:317, 26:145, 4:128, 34:97, 32:90, 25:83, 29:71, 15:70, 2:60, 31:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=317 fs=2 fl=1 hz=0.005961251862891207, 26:ds=145 fs=3 fl=1 hz=0.008680555555555556, 4:ds=128 fs=18 fl=1 hz=0.02243211334120425, 34:ds=97 fs=14 fl=3 hz=0.019144144144144143, 32:ds=90 fs=2 fl=0 hz=0.008450704225352114, 25:ds=83 fs=21 fl=0 hz=0.023836549375709424, 29:ds=71 fs=27 fl=0 hz=0.030100334448160536, 15:ds=70 fs=15 fl=1 hz=0.019698725376593278, 2:ds=60 fs=23 fl=2 hz=0.028344671201814057, 31:ds=57 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=97 flags=blue+purple
- S8: ds=74 flags=red+purple
- S20: ds=57 flags=purple
- S3: ds=44 flags=blue+purple
- S24: ds=40 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:703(B); evening:900(B)
- 445 -> combined:779(B); evening:695(B)
- 459 -> combined:688(B); midday:860(B)
- 888 -> combined:711(B); evening:703(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:48(purple); midday:29(purple)
- 15 -> combined:27(purple); evening:32(purple)
- 25 -> combined:47(blue); evening:47(blue)
- 44 -> combined:97(blue); evening:118(red); midday:48(purple)
- 48 -> combined:84(red); evening:42(blue); midday:44(blue)
- 49 -> combined:78(red); evening:39(blue); midday:48(blue)
- 78 -> combined:80(red); evening:40(blue); midday:74(red)
- 88 -> combined:34(purple); midday:56(purple)
- 99 -> combined:78(blue); evening:39(purple); midday:96(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(3.0155142857142856)[R1,XVAR-Cons(CE)], 7(1.5955714285714284)[R1,Double-Pressure], 9(1.327)[R1,Double-Pressure], 4(1.008)[R2,Double-Pressure], 5(0.9925999999999999)[R2,Double-Pressure]
- P2: 4(4.094771428571429)[R1,Mirror-Echo], 9(4.039571428571429)[R2,Mirror-Echo], 2(1.8168000000000002)[R3,XVAR-Cons(CE)], 0(1.6749642857142855)[R1,Mirror-Echo], 8(0.9925999999999999)[R2,Double-Pressure]
- P3: 4(7.665685714285714)[R1,XVAR-Cons(CEM)], 2(2.8212857142857146)[R3,XVAR-Cons(CE)], 5(2.42405)[R2,XVAR-Cons(CM)], 8(1.0553)[R2,Double-Pressure], 7(0.8998999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-06.xlsm aux_state_label=Connecticut; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:8(gap=24), P2:4(gap=19), P3:4(gap=32); top cartesian candidates: 844, 894, 444, 494, 744.
- Q3: Blackapple: score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '8', '9'], 'pairs': {'remaining_count': 0}}; top candidates: 012, 014, 018, 019, 023.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 133→combined:703(B),evening:900(B); 445→combined:779(B),evening:695(B); 459→combined:688(B),midday:860(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 16:413, 32:180, 25:166, 29:139, 4:137.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=156 Evening=553; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 156 (post-hoc); Stable exact_boxed=False
- Candidate universe (Evening): BOX 355 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 156 (canon 156): box `156` covers winner `156` (boxed hit).
  - Evening winner 553 (canon 355): box `355` covers winner `553` (boxed hit).
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
