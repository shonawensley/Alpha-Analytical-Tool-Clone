# Master Validation Run Report — OntarioCanada4 — results 2026-01-03 (history workbook ~ 2026-01-02)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-03/OntarioCanada4/`
- Winners lens: `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2026-01-03/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2026-01-03/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2026-01-03/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2026-01-03/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2026-01-03/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2026-01-03/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_032_20260105_054559.html`
- `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_968_20260105_054557.html`

Winners JSON files:
- `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_032_20260105_054559.json`
- `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_968_20260105_054557.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-03/OntarioCanada4/winners/OntarioCanada4/digest.md`.
- Q2: Stable environment quick read: Midday 968 (canon 689): exact_boxed=True exact_straight=True | rank 1284/4859 (rank_frac 0.264); Evening 032 (canon 023): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 032 idx11 (rank 8/35, frac 0.229), 968 idx24 (rank 24/35, frac 0.686)
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

### 2.Stable — OntarioCanada4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2026-01-03)

## Midday winner 968 (canonical 689)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=7 | family_rows=162 | exact_boxed=7 | exact_straight=7 | vt_boxed=7
- Scores (patterns_scores.csv): rank 1284/4859 (rank_frac 0.26425190368388557) | score 14.5 (top 37.5, ratio 0.38666666666666666, delta 23.0) | section Combined, Set Set1, Draw Draw5, Col 2, hot 2, vt_straight 2.0 | why straight|cov1|hot2|hidden3v|vtrac_straight|set_chain3
- Compound (patterns_compound.csv): rank 255/1804 (rank_frac 0.14135254988913526) | score 21.5 (top 74.5, ratio 0.28859060402684567, delta 53.0) | section Combined, col1_hits 0, hot2 1, set_chain 3, draw_chain 1 | why set_chain3|draw_chain1|hot2x1|vstrx1
- Families (patterns_families.csv): count 23 | rank 282/1288 (rank_frac 0.21894409937888198) | score 20.0 (top 29.5, ratio 0.6779661016949152, delta 9.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=157

## Evening winner 032 (canonical 023)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=555 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): count 61 | rank 33/1288 (rank_frac 0.02562111801242236) | score 25.5 (top 29.5, ratio 0.864406779661017, delta 4.0) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=85
- Coverage gaps: missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank   11 | canon 267 | section Midday | score 50.5 | col1_hits 4 | hot2 8
- rank    6 | canon 677 | section Midday | score 57.5 | col1_hits 5 | hot2 6
- rank   25 | canon 246 | section Midday | score 42.5 | col1_hits 5 | hot2 6
- rank    7 | canon 477 | section Midday | score 56.0 | col1_hits 5 | hot2 6
- rank    1 | canon 188 | section Evening | score 74.5 | col1_hits 2 | hot2 6
- rank    3 | canon 1188 | section Evening | score 64.0 | col1_hits 2 | hot2 6
- rank    2 | canon 118 | section Evening | score 74.0 | col1_hits 2 | hot2 6
- rank   50 | canon 256 | section Midday | score 34.5 | col1_hits 0 | hot2 5
- rank   32 | canon 047 | section Combined | score 40.0 | col1_hits 3 | hot2 5
- rank   25 | canon 167 | section Combined | score 42.5 | col1_hits 0 | hot2 5

## Top families (patterns_families.csv)
- rank 1226 | family 14 | score 6.0 | hot2 0 | section Midday
- rank  316 | family 21 | score 19.5 | hot2 0 | section Midday
- rank  587 | family 22 | score 15.5 | hot2 5 | section Midday
- rank  658 | family 7 | score 14.5 | hot2 3 | section Midday
- rank  658 | family 10 | score 14.5 | hot2 3 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 968 (canon 689): exact_boxed=True exact_straight=True | rank 1284/4859 (rank_frac 0.264); Evening 032 (canon 023): exact_boxed=False exact_straight=False | rank N/A (rank_frac N/A)
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

### 2.Digit Reduction — OntarioCanada4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20260105)

## Midday winner 968 (canonical 689)
- Stamp (winner_stamp.json): items_total=134 | exact_any=0 exact_final=0 | vtrac_any=134 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=29 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=134 | exact_any=0 vtrac_any=134 | drop_exact_any=0 drop_vtrac_any=29 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=17 vt_straight=0
- Hits (winner_hits.csv): rows=134 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=17 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=9.727143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 032 (canonical 023)
- Stamp (winner_stamp.json): items_total=9 | exact_any=0 exact_final=0 | vtrac_any=9 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=9 | exact_any=0 vtrac_any=9 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=9 vt_straight=0
- Hits (winner_hits.csv): rows=9 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=9 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=24 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.797143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 968 (canonical 689)
- Stamp (winner_stamp.json): items_total=142 | exact_any=0 exact_final=0 | vtrac_any=142 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=29 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=142 | exact_any=0 vtrac_any=142 | drop_exact_any=0 drop_vtrac_any=29 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=25 vt_straight=0
- Hits (winner_hits.csv): rows=142 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=25 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.777143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 12.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 12.277143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 12.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 11.877143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 11.577143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 11.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 11.077143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 992 | score_v2 10.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 992 | score_v2 10.937143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 992 | score_v2 12.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 992 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 594 | score_v2 10.797143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 559 | score_v2 10.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 552 | score_v2 10.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 559 | score_v2 9.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 552 | score_v2 9.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 940 | score_v2 9.647143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 924 | score_v2 9.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 552 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 968 (canon 689): items_total=134 exact_any=0 vtrac_any=134 | top winner_present=False best_rank=None/22; Evening 032 (canon 023): items_total=9 exact_any=0 vtrac_any=9 | top winner_present=False best_rank=None/24; Combined 968 (canon 689): items_total=142 exact_any=0 vtrac_any=142 | top winner_present=False best_rank=None/26
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 992, 992, 594, 559, 552.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20260105_054821)

## Top indices (from enhanced JSON)
- index 10 | score 45.943775 | features: presence=30.926275000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 7 | score 41.09260750000001 | features: presence=22.415107500000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 3 | score 36.148876666666666 | features: presence=26.254710000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 35.64415 | features: presence=21.75665, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 2 | score 21.0184725 | features: presence=11.040972500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 17 | score 17.846112500000004 | features: presence=9.898612500000002, cross_section=0.5, set_echo=0.3, first_hit=0.2
- index 6 | score 11.117862500000003 | features: presence=5.660362500000001, cross_section=0.5, set_echo=0.3, first_hit=0.2
- index 11 | score 10.474208333333332 | features: presence=3.13525, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 21 | score 8.971408333333331 | features: presence=2.68245, cross_section=0.5, set_echo=0.3, first_hit=0.13333333333333336
- index 23 | score 8.937058333333335 | features: presence=2.6081000000000008, set_echo=0.6, first_hit=0.13333333333333336, column_span=0.06562499999999999

## Top straights (from enhanced JSON)
267, 675, 567, 752, 762, 027, 257, 072, 526, 625

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 032 | index 11 | file OntarioCanada4_vtrac11_winner_032_20260105_054559.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 968 | index 24 | file OntarioCanada4_vtrac24_winner_968_20260105_054557.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 032 | index 11 rank 8/35 (rank_frac 0.22857142857142856) | score 10.474208333333332 (top 45.943775, ratio 0.22797883572547817, delta 35.46956666666667) | winner_in_index_straights=False | top_index_straights: 253 (1.889), 532 (1.768), 203 (1.225)
- winner 968 | index 24 rank 24/35 (rank_frac 0.6857142857142857) | score 3.125525 (top 45.943775, ratio 0.06802934673957461, delta 42.81825) | winner_in_index_straights=False | top_index_straights: 436 (0.399), 634 (0.375)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 032→idx11 rank 8/35 (frac 0.229); 968→idx24 rank 24/35 (frac 0.686).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 10, 7, 3, 20, 2.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — OntarioCanada4 — 2026-01-03

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2026-01-03)

## Midday winner 968 (canonical 689)
- Top lanes (hot_zones_top_lanes.csv): present | rank 171/210 (rank_frac 0.8142857142857143) | score_mean 16.045 (top 21.912, ratio 0.7322471705001826, delta 5.866999999999997)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 032 (canonical 023)
- Top lanes (hot_zones_top_lanes.csv): present | rank 90/210 (rank_frac 0.42857142857142855) | score_mean 17.155 (top 21.912, ratio 0.7829043446513327, delta 4.756999999999998)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 035 | vt_triad 114 | score_mean 21.912 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 267 | vt_triad 233 | score_mean 21.55 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 237 | vt_triad 334 | score_mean 20.648 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 127 | vt_triad 233 | score_mean 20.293 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    5 | triad 279 | vt_triad 335 | score_mean 20.114 | tags col1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 557 | vt_triad 13 | score_mean 19.791 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 118 | vt_triad 24 | score_mean 19.745 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 239 | vt_triad 345 | score_mean 19.63 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 188 | vt_triad 24 | score_mean 19.621 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 258 | vt_triad 134 | score_mean 19.612 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 968 (canon 689): rank 171/210 (rank_frac 0.814) ratio_to_top=0.7322471705001826; Evening 032 (canon 023): rank 90/210 (rank_frac 0.429) ratio_to_top=0.7829043446513327
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

Aux draws snapshot dir: `sharepacks/2026-01-03/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=816, 053, 546, 528, 932
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=053, 528, 918, 409, 006
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=816, 546, 932, 372, 043

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=52 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:8 (gap=24), P3:4 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=923 sev=B
- 555: ds=888 sev=B
- 039: ds=779 sev=B
- 333: ds=750 sev=B
- 188: ds=723 sev=B
- 266: ds=709 sev=B
- 477: ds=707 sev=B
- 126: ds=699 sev=B
- 669: ds=694 sev=B
- 007: ds=684 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=125 sev=red
  - 55: ds=81 sev=blue
  - 11: ds=40 sev=purple
  - 88: ds=34 sev=purple
  - 44: ds=25 sev=purple
  - 77: ds=16 sev=-
  - 99: ds=13 sev=-
  - 66: ds=12 sev=-
  - 33: ds=11 sev=-
  - 00: ds=9 sev=-
- non_repeating:
  - 01: ds=60 sev=red
  - 15: ds=57 sev=red
  - 17: ds=51 sev=blue
  - 12: ds=37 sev=blue
  - 69: ds=36 sev=purple
  - 24: ds=35 sev=purple
  - 26: ds=35 sev=purple
  - 67: ds=32 sev=purple
  - 36: ds=29 sev=purple
  - 48: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:335, 16:289, 17:161, 20:139, 33:85, 12:84, 26:79, 34:66, 8:62, 7:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=335 fs=1 fl=0 hz=0.005698005698005698, 16:ds=289 fs=2 fl=0 hz=0.006329113924050633, 17:ds=161 fs=19 fl=1 hz=0.024242424242424242, 20:ds=139 fs=13 fl=2 hz=0.01847290640394089, 33:ds=85 fs=24 fl=1 hz=0.027472527472527472, 12:ds=84 fs=45 fl=0 hz=0.04928806133625411, 26:ds=79 fs=2 fl=1 hz=0.006075334143377886, 34:ds=66 fs=14 fl=2 hz=0.019698725376593278, 8:ds=62 fs=39 fl=2 hz=0.044956140350877194, 7:ds=46 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=80 flags=blue+purple
- S21: ds=77 flags=purple
- S4: ds=71 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 037: score=3 tags=FLT,RS
  - 136: score=3 tags=MIR,RS
  - 379: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 027: score=2 tags=FLT,MIR
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=2 last_repeat_gap=18 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:7 (gap=24), P3:0 (gap=16)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=996 sev=B
- 333: ds=979 sev=B
- 255: ds=946 sev=B
- 355: ds=911 sev=B
- 466: ds=832 sev=B
- 446: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=62 sev=purple
  - 55: ds=40 sev=purple
  - 11: ds=30 sev=purple
  - 77: ds=23 sev=-
  - 88: ds=19 sev=-
  - 66: ds=14 sev=-
  - 44: ds=12 sev=-
  - 99: ds=6 sev=-
  - 33: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 34: ds=71 sev=red
  - 07: ds=68 sev=red
  - 16: ds=54 sev=blue
  - 39: ds=42 sev=blue
  - 68: ds=38 sev=blue
  - 37: ds=37 sev=blue
  - 67: ds=37 sev=blue
  - 48: ds=34 sev=purple
  - 01: ds=30 sev=purple
  - 69: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:167, 34:162, 16:144, 27:99, 12:96, 14:81, 17:80, 20:69, 19:54, 33:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=167 fs=4 fl=3 hz=0.010432190760059612, 34:ds=162 fs=8 fl=4 hz=0.014423076923076924, 16:ds=144 fs=3 fl=0 hz=0.007462686567164179, 27:ds=99 fs=15 fl=2 hz=0.0189520624303233, 12:ds=96 fs=45 fl=0 hz=0.05079006772009029, 14:ds=81 fs=39 fl=0 hz=0.04276315789473684, 17:ds=80 fs=29 fl=2 hz=0.033879781420765025, 20:ds=69 fs=24 fl=3 hz=0.029315960912052113, 19:ds=54 fs=20 fl=2 hz=0.023732470334412083, 33:ds=42 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=78 flags=purple
- S25: ds=74 flags=purple
- S1: ds=63 flags=blue+purple
- S5: ds=61 flags=purple
- S9: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=55 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=14), P2:6 (gap=16), P3:9 (gap=40)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=903 sev=B
- 113: ds=854 sev=B
- 378: ds=847 sev=B
- 566: ds=836 sev=B
- 199: ds=828 sev=B
- 899: ds=806 sev=B
- 126: ds=802 sev=B
- 559: ds=797 sev=B
- 477: ds=786 sev=B
- 558: ds=752 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=232 sev=red
  - 22: ds=63 sev=purple
  - 00: ds=50 sev=purple
  - 44: ds=33 sev=purple
  - 11: ds=20 sev=-
  - 99: ds=18 sev=-
  - 88: ds=17 sev=-
  - 33: ds=15 sev=-
  - 77: ds=8 sev=-
  - 66: ds=6 sev=-
- non_repeating:
  - 36: ds=75 sev=red
  - 24: ds=59 sev=red
  - 89: ds=53 sev=blue
  - 15: ds=52 sev=blue
  - 78: ds=51 sev=blue
  - 49: ds=45 sev=blue
  - 57: ds=42 sev=blue
  - 09: ds=32 sev=purple
  - 01: ds=30 sev=purple
  - 12: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:428, 1:343, 16:194, 26:126, 17:104, 20:95, 3:74, 23:67, 33:65, 31:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=428 fs=0 fl=2 hz=0.005366726296958855, 1:ds=343 fs=0 fl=0 hz=0.0, 16:ds=194 fs=3 fl=1 hz=0.007853403141361256, 26:ds=126 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=104 fs=13 fl=3 hz=0.018626309662398137, 20:ds=95 fs=15 fl=2 hz=0.01925254813137033, 3:ds=74 fs=15 fl=4 hz=0.02092511013215859, 23:ds=67 fs=25 fl=2 hz=0.03085714285714286, 33:ds=65 fs=27 fl=1 hz=0.030803080308030802, 31:ds=61 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=84 flags=purple
- S2: ds=74 flags=blue+purple
- S4: ds=72 flags=purple
- S25: ds=61 flags=purple
- S20: ds=54 flags=purple
- S9: ds=52 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=MIR
  - 016: score=1 tags=MIR
  - 025: score=1 tags=MIR
  - 027: score=1 tags=MIR
  - 035: score=1 tags=MIR
  - 038: score=1 tags=MIR
  - 045: score=1 tags=MIR
  - 049: score=1 tags=MIR
  - 056: score=1 tags=MIR
  - 057: score=1 tags=MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:699(B); evening:802(B)
- 128 -> combined:923(B); evening:903(B)
- 333 -> combined:750(B); midday:979(B)
- 477 -> combined:707(B); evening:786(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:60(red); evening:30(purple); midday:30(purple)
- 11 -> combined:40(purple); midday:30(purple)
- 12 -> combined:37(blue); evening:30(purple)
- 15 -> combined:57(red); evening:52(blue); midday:28(purple)
- 17 -> combined:51(blue); evening:26(purple); midday:25(purple)
- 22 -> combined:125(red); evening:63(purple); midday:62(purple)
- 24 -> combined:35(purple); evening:59(red)
- 36 -> combined:29(purple); evening:75(red)
- 44 -> combined:25(purple); evening:33(purple)
- 48 -> combined:28(purple); midday:34(purple)
- 55 -> combined:81(blue); evening:232(red); midday:40(purple)
- 67 -> combined:32(purple); midday:37(blue)
- 69 -> combined:36(purple); midday:29(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.882128571428572)[R1,Mirror-Echo], 7(5.766507142857143)[R2,XVAR-Cons(CEM)], 2(1.3420642857142857)[R2,Mirror-Echo], 4(1.088)[R1,Double-Pressure], 6(0.6411428571428572)[R3,Mirror-Echo]
- P2: 8(7.169364285714286)[R1,XVAR-Cons(CEM)], 6(3.565714285714286)[R2,XVAR-Cons(CE)], 7(1.4165714285714284)[R1,Double-Pressure], 3(0.3282928571428571)[R3,Mirror-Echo], 9(0.2414285714285714)[R3,Swap]
- P3: 4(6.276914285714286)[R1,XVAR-Cons(CEM)], 1(2.6984285714285714)[R3,XVAR-Cons(CE)], 9(1.8427142857142857)[R1,Mirror-Echo], 0(1.0777142857142856)[R1,Double-Pressure], 5(1.018)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-02.xlsm aux_state_label=Ontario; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:1(gap=26), P2:8(gap=24), P3:4(gap=25); top cartesian candidates: 184, 784, 181, 164, 781.
- Q3: Blackapple: score=2 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}; top candidates: 127, 037, 136, 379, 469.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 126→combined:699(B),evening:802(B); 128→combined:923(B),evening:903(B); 333→combined:750(B),midday:979(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 1:335, 16:289, 17:161, 20:139, 33:85.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=968 Evening=032; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 689 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 023 (post-hoc); Stable exact_boxed=False
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
  - Midday winner 968 (canon 689): box `689` covers winner `968` (boxed hit).
  - Evening winner 032 (canon 023): box `023` covers winner `032` (boxed hit).
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
