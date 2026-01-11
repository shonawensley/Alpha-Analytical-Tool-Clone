# Master Validation Run Report — NorthCarolina4 — results 2026-01-06 (history workbook ~ 2026-01-05)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2026-01-06/NorthCarolina4/`
- Winners lens: `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2026-01-06/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2026-01-06/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2026-01-06/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2026-01-06/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2026-01-06/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2026-01-06/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac30_winner_298_20260107_052310.html`
- `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_552_20260107_052309.html`

Winners JSON files:
- `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac30_winner_298_20260107_052310.json`
- `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac3_winner_552_20260107_052309.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Winners lens digest: `sharepacks/2026-01-06/NorthCarolina4/winners/NorthCarolina4/digest.md`.
- Q2: Stable environment quick read: Midday 552 (canon 255): exact_boxed=True exact_straight=True | rank 1222/6487 (rank_frac 0.188); Evening 298 (canon 289): exact_boxed=True exact_straight=True | rank 4466/6487 (rank_frac 0.688)
- Q3: VTRAC index placement (Brain-1 VTRAC enhanced): 298 idx30 (rank 33/35, frac 0.943), 552 idx3 (rank 13/35, frac 0.371)
- Q4: Variant bias (first pass): use Stable exact-hit + Hot Zones rank fractions; verdict below.
- Q5: Permutation lane clarity: defer to Part 2 VTRAC + Part A winners HTML; record any tight VT family vs diffuse lanes in Part 5.
- Q6: Environment verdict: **strong (Stable exact boxed hits)**.
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

### 2.Stable — NorthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2026-01-06)

## Midday winner 552 (canonical 255)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=20 | family_rows=83 | exact_boxed=20 | exact_straight=17 | vt_boxed=20
- Scores (patterns_scores.csv): rank 1222/6487 (rank_frac 0.18837675350701402) | score 19.0 (top 42.0, ratio 0.4523809523809524, delta 23.0) | section Midday, Set Set1, Draw Draw4, Col 2, hot 2, vt_straight 2.0 | why straight|cov2|hp_repeat3|vstr2|hot2|double_mirror|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 188/1721 (rank_frac 0.10923881464264962) | score 30.0 (top 101.5, ratio 0.2955665024630542, delta 71.5) | section Midday, col1_hits 0, hot2 2, set_chain 1, draw_chain 3 | why draw_chain3|hot2x2|vstrx5|dblmirrorx6
- Families (patterns_families.csv): count 33 | rank 656/1636 (rank_frac 0.40097799511002447) | score 19.0 (top 40.5, ratio 0.4691358024691358, delta 21.5) | section Evening, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=17

## Evening winner 298 (canonical 289)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=6 | family_rows=285 | exact_boxed=6 | exact_straight=6 | vt_boxed=6
- Scores (patterns_scores.csv): rank 4466/6487 (rank_frac 0.6884538307383998) | score 12.0 (top 42.0, ratio 0.2857142857142857, delta 30.0) | section Midday, Set Set1, Draw Draw2, Col 3, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot1|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 498/1721 (rank_frac 0.28936664729808254) | score 19.0 (top 101.5, ratio 0.18719211822660098, delta 82.5) | section Midday, col1_hits 0, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|hot1x3|vstrx3
- Families (patterns_families.csv): count 51 | rank 435/1636 (rank_frac 0.2658924205378973) | score 22.0 (top 40.5, ratio 0.5432098765432098, delta 18.5) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=56

## Top compound candidates (patterns_compound.csv)
- rank   15 | canon 266 | section Combined | score 81.0 | col1_hits 7 | hot2 11
- rank    8 | canon 022 | section Midday | score 91.0 | col1_hits 7 | hot2 11
- rank    1 | canon 229 | section Midday | score 101.5 | col1_hits 9 | hot2 11
- rank   21 | canon 2299 | section Midday | score 73.5 | col1_hits 7 | hot2 11
- rank   22 | canon 02299 | section Midday | score 73.0 | col1_hits 7 | hot2 11
- rank   14 | canon 299 | section Midday | score 83.0 | col1_hits 7 | hot2 11
- rank   19 | canon 099 | section Midday | score 76.5 | col1_hits 7 | hot2 11
- rank   11 | canon 0229 | section Midday | score 84.0 | col1_hits 7 | hot2 11
- rank   19 | canon 2246 | section Combined | score 76.5 | col1_hits 7 | hot2 11
- rank    4 | canon 224 | section Combined | score 99.0 | col1_hits 7 | hot2 11

## Top families (patterns_families.csv)
- rank 1629 | family 16 | score 4.0 | hot2 0 | section Midday
- rank   18 | family 28 | score 36.5 | hot2 2 | section Midday
- rank  687 | family 25 | score 18.5 | hot2 0 | section Midday
- rank  656 | family 10 | score 19.0 | hot2 0 | section Midday
- rank  602 | family 15 | score 19.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 552 (canon 255): exact_boxed=True exact_straight=True | rank 1222/6487 (rank_frac 0.188); Evening 298 (canon 289): exact_boxed=True exact_straight=True | rank 4466/6487 (rank_frac 0.688)
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

### 2.Digit Reduction — NorthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20260107)

## Midday winner 552 (canonical 255)
- Stamp (winner_stamp.json): items_total=70 | exact_any=0 exact_final=0 | vtrac_any=70 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=15 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=70 | exact_any=0 vtrac_any=70 | drop_exact_any=0 drop_vtrac_any=15 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=26 vt_straight=0
- Hits (winner_hits.csv): rows=70 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=26 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=8 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=14.177143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 298 (canonical 289)
- Stamp (winner_stamp.json): items_total=2 | exact_any=0 exact_final=0 | vtrac_any=2 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=2 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=2 | exact_any=0 vtrac_any=2 | drop_exact_any=0 drop_vtrac_any=2 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=2 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=20 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=13.127143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 552 (canonical 255)
- Stamp (winner_stamp.json): items_total=146 | exact_any=36 exact_final=0 | vtrac_any=144 vtrac_final=26 | drop_exact_any=36 drop_exact_final=0 | drop_vtrac_any=82 drop_vtrac_final=26 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=40 family_vtrac_final=0
- Flags (winner_flags.csv): rows=146 | exact_any=36 vtrac_any=144 | drop_exact_any=36 drop_vtrac_any=82 | family_exact_any=0 family_vtrac_any=40 | vt_boxed=66 vt_straight=0
- Hits (winner_hits.csv): rows=146 | exact_final=0 vtrac_final=26 | drop_exact_final=0 drop_vtrac_final=26 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=66 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=8 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.015714 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 992 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 992 | score_v2 14.177143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 992 | score_v2 13.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 7 | pattern 922 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 4 | pattern 992 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw7 col 1 | pattern 992 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 992 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 6 | pattern 992 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 5 | pattern 992 | score_v2 13.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 5 | pattern 992 | score_v2 13.877143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 992 | score_v2 14.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 922 | score_v2 13.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 224 | score_v2 13.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 224 | score_v2 12.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 992 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 992 | score_v2 11.015714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 10.032597 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 992 | score_v2 10.015714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 922 | score_v2 9.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 922 | score_v2 9.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 552 (canon 255): items_total=70 exact_any=0 vtrac_any=70 | top winner_present=False best_rank=None/8; Evening 298 (canon 289): items_total=2 exact_any=0 vtrac_any=2 | top winner_present=False best_rank=None/20; Combined 552 (canon 255): items_total=146 exact_any=36 vtrac_any=144 | top winner_present=False best_rank=None/8
- Q2: 4 hit criteria: DR supports exact/vtrac/drop/family paths via stamp counts; treat vt_boxed/vt_straight as the realistic hedge.
- Q3: Winners artifacts alignment: stamp/flags/hits should be internally consistent (validator-driven).
- Q4: Dominance/noise: use items_total + vt_boxed counts; zero items_total with winners present is a red flag.
- Q5: Top DR candidates (best_pattern): 992, 922, 224, 224, 992.
- Q6: Miss analysis: winner_present=False usually means DR didn’t isolate; treat as tool outcome unless gaps listed.
- Q7: Validation (V): if variant shows gaps or missing analyzer_v2 files, flag Fix-Now; otherwise OK.
- Q8: Optimization notes: consider whether vt_boxed should be promoted in pack translation when DR is strong.
- Q9: Cross-tool synergy: compare DR top patterns with Stable compound canonicals and Hot Zones lanes (shared digits/VT).
- Q10: Takeaway: DR is primarily an environment + VT-hedge lens; record whether it isolated or not for later tuning.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20260107_052525)

## Top indices (from enhanced JSON)
- index 28 | score 104.62108499999997 | features: presence=72.32358499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 79.28169999999996 | features: presence=54.79419999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 64.79583499999997 | features: presence=46.76833499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 46.369764999999994 | features: presence=27.852264999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 40.19715 | features: presence=27.069650000000003, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 39.6289275 | features: presence=29.471427500000004, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 12 | score 30.947214999999996 | features: presence=17.819715, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 24.07855 | features: presence=14.921050000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 2 | score 22.976650000000006 | features: presence=12.549150000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 19 | score 22.52265 | features: presence=15.285149999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4

## Top straights (from enhanced JSON)
092, 259, 290, 019, 659, 901, 109, 962, 592, 159

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 298 | index 30 | file NorthCarolina4_vtrac30_winner_298_20260107_052310.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 552 | index 3 | file NorthCarolina4_vtrac3_winner_552_20260107_052309.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 298 | index 30 rank 33/35 (rank_frac 0.9428571428571428) | score 0.0 (top 104.62108499999997, ratio 0.0, delta 104.62108499999997) | winner_in_index_straights=False | top_index_straights: (none)
- winner 552 | index 3 rank 13/35 (rank_frac 0.37142857142857144) | score 16.152150000000002 (top 104.62108499999997, ratio 0.1543871390743081, delta 88.46893499999996) | winner_in_index_straights=False | top_index_straights: 250 (2.365), 052 (2.314)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: winner index placements: 298→idx30 rank 33/35 (frac 0.943); 552→idx3 rank 13/35 (frac 0.371).
- Q2: 4 hit criteria: VTRAC’s direct path is VT-straight/VT-boxed. Use index placement + top indices as the actionable lane set.
- Q3: Winners lens alignment: winners_lens JSON/HTML should exist; treat rank/score=0 as ‘cold’ within family stats, not missing data.
- Q4: Dominance/noise: if winner index is outside top ranks, treat as weak VTRAC isolation; if inside top-5, treat as strong.
- Q5: Top indices (enhanced): 28, 20, 31, 10, 25.
- Q6: Miss analysis: low index placement is a tool outcome; do not fix via wiring unless day-level VTRAC payload missing.
- Q7: Validation (V): vtrac_compact_report should be non-empty; validation_report should exist.
- Q8: Optimization notes: avoid tuning clamps until corpus is larger; rely on implied_set grading for alerts.
- Q9: Cross-tool synergy: when Stable/DR/HotZones also tag vt-straight/VT family, boost the lane in pack translation.
- Q10: Takeaway: treat VTRAC as ‘lane selection’ evidence and track index placement distributions across days.

---

### 2.Hot Zones — NorthCarolina4 — 2026-01-06

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2026-01-06)

## Midday winner 552 (canonical 255)
- Top lanes (hot_zones_top_lanes.csv): present | rank 75/206 (rank_frac 0.3640776699029126) | score_mean 16.846 (top 22.795, ratio 0.7390217152884404, delta 5.949000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 298 (canonical 289)
- Top lanes (hot_zones_top_lanes.csv): present | rank 74/206 (rank_frac 0.3592233009708738) | score_mean 16.878 (top 22.795, ratio 0.7404255319148936, delta 5.917000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 355 | vt_triad 14 | score_mean 22.795 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    2 | triad 338 | vt_triad 44 | score_mean 22.486 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 033 | vt_triad 14 | score_mean 20.452 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vt_straight
- rank    4 | triad 347 | vt_triad 345 | score_mean 20.429 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 178 | vt_triad 234 | score_mean 20.299 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 788 | vt_triad 34 | score_mean 20.289 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_straight
- rank    7 | triad 224 | vt_triad 35 | score_mean 20.284 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical3,vt_straight
- rank    8 | triad 011 | vt_triad 12 | score_mean 20.196 | tags hot16,hot20,set1_bonus,straight_lane,vertical2,vertical3
- rank    9 | triad 667 | vt_triad 23 | score_mean 19.838 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank   10 | triad 229 | vt_triad 35 | score_mean 19.829 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence: Midday 552 (canon 255): rank 75/206 (rank_frac 0.364) ratio_to_top=0.7390217152884404; Evening 298 (canon 289): rank 74/206 (rank_frac 0.359) ratio_to_top=0.7404255319148936
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

Aux draws snapshot dir: `sharepacks/2026-01-06/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2026-01-06

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-06/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-05.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-06/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=895, 553, 887, 187, 178
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-06/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=553, 187, 374, 033, 416
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-06/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=895, 887, 178, 383, 053

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=4 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=23), P2:4 (gap=41), P3:2 (gap=38)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=52.96662142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 240: score=46.79148857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 942: score=44.22774285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 202: score=43.85948428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 940: score=42.22257142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=38.291171428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 200: score=37.68435142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 292: score=37.52232857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 902: score=35.85197142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=34.03800714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=884 sev=B
- 446: ds=880 sev=B
- 445: ds=820 sev=B
- 122: ds=803 sev=B
- 036: ds=799 sev=B
- 555: ds=776 sev=B
- 299: ds=773 sev=B
- 277: ds=765 sev=B
- 112: ds=754 sev=B
- 034: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=160 sev=red
  - 77: ds=133 sev=red
  - 99: ds=56 sev=purple
  - 44: ds=54 sev=purple
  - 22: ds=20 sev=-
  - 11: ds=16 sev=-
  - 66: ds=15 sev=-
  - 33: ds=6 sev=-
  - 88: ds=2 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 56: ds=62 sev=red
  - 27: ds=58 sev=red
  - 02: ds=52 sev=blue
  - 23: ds=48 sev=blue
  - 09: ds=47 sev=blue
  - 28: ds=44 sev=blue
  - 04: ds=41 sev=blue
  - 06: ds=41 sev=blue
  - 29: ds=38 sev=blue
  - 24: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:488, 1:115, 27:111, 31:102, 15:86, 16:84, 10:74, 23:63, 35:54, 12:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=488 fs=3 fl=0 hz=0.009389671361502348, 1:ds=115 fs=0 fl=3 hz=0.00625, 27:ds=111 fs=15 fl=2 hz=0.02463768115942029, 31:ds=102 fs=19 fl=3 hz=0.02502844141069397, 15:ds=86 fs=16 fl=2 hz=0.019758507135016465, 16:ds=84 fs=4 fl=1 hz=0.008836524300441826, 10:ds=74 fs=21 fl=2 hz=0.027315914489311165, 23:ds=63 fs=17 fl=3 hz=0.024330900243309, 35:ds=54 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=52 fs=46 fl=1 hz=0.049893842887473464

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=96 flags=purple
- S4: ds=55 flags=purple
- S7: ds=37 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 027: score=3 tags=FLT,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=2 last_repeat_gap=100 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=39), P2:9 (gap=29), P3:2 (gap=42)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=52.96662142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 240: score=46.79148857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 942: score=44.22774285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 202: score=43.85948428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 940: score=42.22257142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=38.291171428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 200: score=37.68435142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 292: score=37.52232857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 902: score=35.85197142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=34.03800714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=977 sev=B
- 123: ds=952 sev=B
- 446: ds=929 sev=B
- 777: ds=889 sev=B
- 119: ds=854 sev=B
- 222: ds=824 sev=B
- 155: ds=786 sev=B
- 488: ds=780 sev=B
- 177: ds=756 sev=B
- 007: ds=735 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=159 sev=red
  - 00: ds=134 sev=red
  - 77: ds=66 sev=purple
  - 99: ds=54 sev=purple
  - 22: ds=42 sev=purple
  - 11: ds=12 sev=-
  - 88: ds=8 sev=-
  - 66: ds=7 sev=-
  - 33: ds=3 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 48: ds=150 sev=red
  - 25: ds=63 sev=red
  - 07: ds=58 sev=red
  - 28: ds=50 sev=blue
  - 23: ds=45 sev=blue
  - 26: ds=45 sev=blue
  - 02: ds=42 sev=blue
  - 29: ds=39 sev=blue
  - 56: ds=33 sev=purple
  - 27: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:382, 25:190, 32:170, 35:144, 11:109, 31:102, 2:98, 33:81, 12:59, 3:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=382 fs=1 fl=0 hz=0.005905511811023622, 25:ds=190 fs=15 fl=1 hz=0.02165087956698241, 32:ds=170 fs=3 fl=1 hz=0.007416563658838071, 35:ds=144 fs=0 fl=2 hz=0.005201560468140442, 11:ds=109 fs=50 fl=0 hz=0.056882821387940846, 31:ds=102 fs=25 fl=0 hz=0.02793296089385475, 2:ds=98 fs=13 fl=3 hz=0.018223234624145785, 33:ds=81 fs=21 fl=2 hz=0.025136612021857924, 12:ds=59 fs=47 fl=0 hz=0.05181918412348401, 3:ds=58 fs=17 fl=2 hz=0.022727272727272728

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=93 flags=purple
- S20: ds=81 flags=red+purple
- S2: ds=72 flags=purple
- S5: ds=68 flags=purple
- S8: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=24 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=18), P2:4 (gap=39), P3:2 (gap=19)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=52.96662142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 240: score=46.79148857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 942: score=44.22774285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 202: score=43.85948428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 940: score=42.22257142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=38.291171428571424 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 200: score=37.68435142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 292: score=37.52232857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 902: score=35.85197142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=34.03800714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=978 sev=B
- 299: ds=935 sev=B
- 223: ds=865 sev=B
- 122: ds=854 sev=B
- 116: ds=831 sev=B
- 039: ds=814 sev=B
- 377: ds=802 sev=B
- 277: ds=788 sev=B
- 188: ds=776 sev=B
- 557: ds=775 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=126 sev=red
  - 77: ds=84 sev=blue
  - 00: ds=80 sev=blue
  - 66: ds=42 sev=purple
  - 99: ds=28 sev=purple
  - 44: ds=27 sev=purple
  - 22: ds=10 sev=-
  - 11: ds=8 sev=-
  - 33: ds=3 sev=-
  - 88: ds=1 sev=-
- non_repeating:
  - 45: ds=103 sev=red
  - 34: ds=44 sev=blue
  - 04: ds=39 sev=blue
  - 06: ds=33 sev=purple
  - 08: ds=32 sev=purple
  - 56: ds=31 sev=purple
  - 27: ds=29 sev=purple
  - 02: ds=26 sev=purple
  - 09: ds=26 sev=purple
  - 23: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:262, 26:244, 13:209, 1:151, 23:120, 5:101, 17:100, 27:57, 31:51, 15:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=262 fs=18 fl=0 hz=0.024896265560165977, 26:ds=244 fs=1 fl=2 hz=0.006666666666666667, 13:ds=209 fs=19 fl=0 hz=0.024675324675324673, 1:ds=151 fs=2 fl=3 hz=0.007434944237918215, 23:ds=120 fs=14 fl=3 hz=0.019384264538198404, 5:ds=101 fs=15 fl=2 hz=0.020809248554913295, 17:ds=100 fs=29 fl=0 hz=0.03553921568627451, 27:ds=57 fs=22 fl=3 hz=0.027085590465872156, 31:ds=51 fs=21 fl=2 hz=0.024338624338624337, 15:ds=43 fs=16 fl=1 hz=0.01829924650161464

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=94 flags=purple
- S0: ds=80 flags=blue+purple
- S4: ds=69 flags=purple
- S2: ds=48 flags=purple
- S21: ds=35 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:799(B); evening:728(B)
- 122 -> combined:803(B); evening:854(B)
- 155 -> combined:884(B); midday:786(B)
- 277 -> combined:765(B); evening:788(B)
- 299 -> combined:773(B); evening:935(B)
- 446 -> combined:880(B); midday:929(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:160(red); evening:80(blue); midday:134(red)
- 02 -> combined:52(blue); evening:26(purple); midday:42(blue)
- 04 -> combined:41(blue); evening:39(blue)
- 06 -> combined:41(blue); evening:33(purple)
- 08 -> combined:31(purple); evening:32(purple)
- 09 -> combined:47(blue); evening:26(purple)
- 23 -> combined:48(blue); midday:45(blue)
- 25 -> combined:36(purple); midday:63(red)
- 27 -> combined:58(red); evening:29(purple); midday:30(purple)
- 28 -> combined:44(blue); midday:50(blue)
- 29 -> combined:38(blue); midday:39(blue)
- 44 -> combined:54(purple); evening:27(purple); midday:159(red)
- 48 -> combined:28(purple); midday:150(red)
- 56 -> combined:62(red); evening:31(purple); midday:33(purple)
- 77 -> combined:133(red); evening:84(blue); midday:66(purple)
- 99 -> combined:56(purple); evening:28(purple); midday:54(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(4.1850000000000005)[R2,XVAR-Cons(CM)], 9(2.5888857142857145)[R3,XVAR-Cons(CM)], 6(2.17065)[R1,XVAR-Cons(CM)], 5(1.2074285714285713)[R1,Double-Pressure], 7(0.9834999999999999)[R2,Double-Pressure]
- P2: 4(8.926571428571428)[R1,XVAR-Cons(CEM)], 0(4.0508)[R2,XVAR-Cons(CE)], 2(2.0247)[R3,XVAR-Cons(CM)], 9(1.7558571428571428)[R1,Mirror-Echo], 3(0.27153571428571427)[R3,Swap]
- P3: 2(8.712285714285713)[R1,XVAR-Cons(CEM)], 0(6.707114285714285)[R2,XVAR-Cons(CEM)], 8(0.5925)[R2,Swap], 4(0.24779285714285712)[R3,Swap], 1(0.22628571428571428)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1: Provenance: excel=data/history/Pick3StatsC4_2026-01-05.xlsm aux_state_label=North Carolina; snapshot_mode=generated_from_excel.
- Q2: Positional pressure (Combined top digits): P1:6(gap=23), P2:4(gap=41), P3:2(gap=38); top cartesian candidates: 242, 240, 942, 202, 940.
- Q3: Blackapple: score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4', '6'], 'pairs': {'remaining_count': 0}}; top candidates: 018, 027, 036, 045, 126.
- Q4: Doubles/pairs: multi-variant doubles alerts (sample): 036→combined:799(B),evening:728(B); 122→combined:803(B),evening:854(B); 155→combined:884(B),midday:786(B).
- Q5: VTRAC overlay (Aux): top overdue indices: 26:488, 1:115, 27:111, 31:102, 15:86.
- Q6: Cross-variant cues: use consensus_notes + Mirror-Echo/Double-Pressure tags in summary block to log repeatable traits.
- Q7: Winner proximity (post-hoc): Midday=552 Evening=298; check whether winners appear in positional/BA candidate lists.
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
- Candidate universe (Midday): BOX 255 (post-hoc); Stable exact_boxed=True
- Candidate universe (Evening): BOX 289 (post-hoc); Stable exact_boxed=True
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
  - Midday winner 552 (canon 255): box `255` covers winner `552` (boxed hit).
  - Evening winner 298 (canon 289): box `289` covers winner `298` (boxed hit).
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
