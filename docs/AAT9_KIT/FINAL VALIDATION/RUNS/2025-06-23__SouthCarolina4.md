# Master Validation Run Report — SouthCarolina4 — results 2025-06-23 (history workbook ~ 2025-06-22)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-23/SouthCarolina4/`
- Winners lens: `sharepacks/2025-06-23/SouthCarolina4/winners/SouthCarolina4/`
- Stable: `sharepacks/2025-06-23/SouthCarolina4/stable/SouthCarolina4/`
- Digit Reduction: `sharepacks/2025-06-23/SouthCarolina4/digit_reduction/SouthCarolina4/`
- VTRAC: `sharepacks/2025-06-23/SouthCarolina4/vtrac/SouthCarolina4/`
- Hot Zones: `sharepacks/2025-06-23/SouthCarolina4/hot_zones/SouthCarolina4/`
- Aux: `sharepacks/2025-06-23/SouthCarolina4/aux/SouthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-06-23/SouthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-23/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_958_20251223_052109.html`
- `sharepacks/2025-06-23/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac24_winner_314_20251223_052111.html`

Winners JSON files:
- `sharepacks/2025-06-23/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac14_winner_958_20251223_052109.json`
- `sharepacks/2025-06-23/SouthCarolina4/winners/SouthCarolina4/SouthCarolina4_vtrac24_winner_314_20251223_052111.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are active with a dense Midday ladder universe and simpler Evening/Combined ladders; winners are primarily narrated by tag density and tool convergence, not by ladder equality.
  - Winners: Midday=958 (canonical 589); Evening=314 (canonical 134) from `data/results/2025-06-23.txt`.
  - Set1/Draw1 ladders (from winners JSON; lens only, not “outcomes”):
    - Midday: col1/col2 `11835** / 51138** / 58311** / 81153**`
    - Evening: col1/col2 `089** / 098**`
    - Combined: col1 `001**`; col2 `015** / 051**`
- Q2: Ladder persistence exists (Midday ladder is a repeated permutation-family of digits 1/1/8/3/5; Evening and Combined are dominated by 0xx ladders like 089/098 and 001/015/051), but ladders are not direct winners (589/134); treat ladders as structure only.
- Q3: Winner tagging (from winners JSON):
  - 958 (canon 589): strongest on-board evidence is Combined (hit-winner=10; hit-winner-gap=35) plus meaningful Evening tagging.
    - Midday: hit-winner=0; hit-winner-gap=0; hit-family=31; hit-family-gap=60.
    - Evening: hit-winner=6; hit-winner-gap=29; hit-family=27; hit-family-gap=96.
    - Combined: hit-winner=10; hit-winner-gap=35; hit-family=32; hit-family-gap=86.
  - 314 (canon 134): unusually strong Midday tagging despite being the Evening winner (cross-variant carry), plus moderate Combined family pressure.
    - Midday: hit-winner=12; hit-winner-gap=67; hit-family=27; hit-family-gap=93.
    - Evening: hit-winner=1; hit-winner-gap=5; hit-family=19; hit-family-gap=46.
    - Combined: hit-winner=2; hit-winner-gap=5; hit-family=49; hit-family-gap=69.
- Q4: Variant bias:
  - 314 shows strong cross-variant carry (Midday tags) even though it hits in Evening, which is consistent with your “bounce” behavior.
  - 958 is more coherent in Evening+Combined tagging rather than Midday tagging.
- Q5: Permutation lane clarity:
  - Both winners have moderate clarity via VTRAC support and tag density, even without substring cells.
- Q6: Environment verdict: **Playable**
  - VTRAC supports both outcomes (958 idx14 rank 2/35; 314 idx24 rank 10/35).
  - Stable supports both at moderate depth (compound rank 139 for 958; compound rank 79 for 314).
- Q7: Hot Zones overlap:
  - 958 best rank 114; 314 best rank 97 (moderate but not isolating; not in top-20 map).
- Q8: Cross-set carryover:
  - Strong cross-variant behavior is present (314 is heavily tagged in Midday; 958 is strongly tagged in Combined).
- Q9: Aux cues (quick lens):
  - Repeat watch current_index (Combined=7, Midday=9, Evening=7) does not match winners’ indices (14/24).
  - BA is low (Combined=2; Midday=1; Evening=0); treat as non-decisive.
- Q10: 4 hit criteria viability (pre-results lens):
  - VTRAC + Stable are the primary channels here; Hot Zones is corroboration only; DR does not isolate.
- Q11: Exact triple presence (winners lens):
  - Literal/canonical substring cells are 0 for both winners; rely on tags + tool evidence.
- Q12: “Profitable environment” summary:
  - This is a good “structure + cross-variant carry” day: both winners are supported by VTRAC placements plus meaningful tag density.
- Q13: Dominance vs dilution:
  - Ladders are structured but not direct; avoid over-weighting ladder equality.
- Q14: Noise check:
  - Moderate (good multi-tool convergence without direct substring evidence).

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — SouthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — SouthCarolina4 (2025-06-23)

## Midday winner 958 (canonical 589)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=9 | family_rows=373 | exact_boxed=9 | exact_straight=4 | vt_boxed=9
- Scores (patterns_scores.csv): rank 915, section Combined, Set Set2, Draw Draw1, Col 4, score 17.0, hot 1, vt_straight 0.0 | why boxed|cov3|hp_repeat4|vstr2|hot1|perm2|set_chain2
- Compound (patterns_compound.csv): rank 139, section Combined, score 28.0, col1_hits 2, hot2 1, set_chain 2, draw_chain 2 | why set_chain2|draw_chain2|col1x2|hot1x3|hot2x1|vstrx2
- Families (patterns_families.csv): 80 rows contain digits; best rank 146, section Combined, score 23.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=138

## Evening winner 314 (canonical 134)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=15 | family_rows=569 | exact_boxed=15 | exact_straight=15 | vt_boxed=15
- Scores (patterns_scores.csv): rank 915, section Midday, Set Set2, Draw Draw1, Col 3, score 17.0, hot 1, vt_straight 2.0 | why straight|cov1|hp_repeat5|hot1|vtrac_straight|set_chain3
- Compound (patterns_compound.csv): rank 79, section Midday, score 34.5, col1_hits 0, hot2 1, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|hot1x8|hot2x1|vstrx5
- Families (patterns_families.csv): 68 rows contain digits; best rank 35, section Combined, score 26.5, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=153

## Top compound candidates (patterns_compound.csv)
- rank    6 | canon 1138 | section Midday | score 77.0 | col1_hits 8 | hot2 11
- rank    1 | canon 113 | section Midday | score 94.5 | col1_hits 8 | hot2 11
- rank    2 | canon 118 | section Midday | score 89.5 | col1_hits 9 | hot2 11
- rank    7 | canon 138 | section Midday | score 76.0 | col1_hits 8 | hot2 11
- rank    9 | canon 358 | section Midday | score 61.5 | col1_hits 7 | hot2 10
- rank    4 | canon 11358 | section Midday | score 82.5 | col1_hits 7 | hot2 10
- rank    3 | canon 115 | section Midday | score 84.0 | col1_hits 7 | hot2 10
- rank    8 | canon 1135 | section Midday | score 70.0 | col1_hits 6 | hot2 10
- rank   13 | canon 1358 | section Midday | score 57.5 | col1_hits 7 | hot2 9
- rank    5 | canon 899 | section Evening | score 81.5 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1414 | family 4 | score 6.5 | hot2 0 | section Midday
- rank  443 | family 4 | score 18.5 | hot2 0 | section Midday
- rank  330 | family 33 | score 20.0 | hot2 0 | section Midday
- rank  219 | family 17 | score 21.5 | hot2 0 | section Midday
- rank  196 | family 21 | score 22.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Both winners are present in Stable scores and compound (958: scores rank 915, compound rank 139; 314: scores rank 915, compound rank 79).
- Q2: 4 hit criteria mapping
  - Stable is a usable corroborator for both outcomes (moderate ranks).
- Q3: Output integrity
  - Stable artifacts exist and show no gaps for either winner.
- Q4: Dominance / noise
  - Stable does not elevate either winner into near-top ranks; treat Stable as supportive rather than dominant.
- Q5: Where the winners show up
  - 314 is the stronger Stable outcome (compound rank 79 vs 139).
- Q6: Miss analysis
  - Stable is not a top-dominant caller but is consistent for both.
- Q7: Validation checks (V)
  - No missing artifacts indicated.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Combine VTRAC index placement + Stable compound rank as a convergence signature (both present here).
- Q10: Analyst’s extra insight
  - Stable provides confirmatory value on this day; it is not sufficient alone.

---

### 2.Digit Reduction — SouthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — SouthCarolina4 (stamp 20251223)

## Midday winner 958 (canonical 589)
- Stamp (winner_stamp.json): items_total=12 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=12 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=12 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=12 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=12 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → None
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 314 (canonical 134)
- Stamp (winner_stamp.json): items_total=68 | exact_any=17 exact_final=0 | vtrac_any=66 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=35 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=13 family_vtrac_final=0
- Flags (winner_flags.csv): rows=68 | exact_any=17 vtrac_any=66 | drop_exact_any=2 drop_vtrac_any=35 | family_exact_any=0 family_vtrac_any=13 | vt_boxed=32 vt_straight=0
- Hits (winner_hits.csv): rows=68 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=32 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 958 (canonical 589)
- Stamp (winner_stamp.json): items_total=217 | exact_any=24 exact_final=0 | vtrac_any=83 vtrac_final=0 | drop_exact_any=60 drop_exact_final=0 | drop_vtrac_any=169 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=55 family_vtrac_final=0
- Flags (winner_flags.csv): rows=217 | exact_any=24 vtrac_any=83 | drop_exact_any=60 drop_vtrac_any=169 | family_exact_any=0 family_vtrac_any=55 | vt_boxed=66 vt_straight=0
- Hits (winner_hits.csv): rows=217 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=66 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 2 | pattern 551 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw4 col 2 | pattern 551 | score_v2 12.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 551 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 511 | score_v2 11.577143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 991 | score_v2 10.577143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 541 | score_v2 10.027143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw2 col 4 | pattern 541 | score_v2 9.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 4 | pattern 541 | score_v2 9.627143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 6 | pattern 592 | score_v2 9.577143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 7 | pattern 592 | score_v2 9.577143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Midday | best_pattern 551 | score_v2 12.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 511 | score_v2 11.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 991 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 541 | score_v2 10.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 541 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 592 | score_v2 9.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 924 | score_v2 9.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 559 | score_v2 9.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 9.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 599 | score_v2 8.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR does not promote either winner into Midday/Evening top candidates (winner_present=False), but Combined winner presence is True for 958 (lens-only).
- Q2: 4 hit criteria mapping
  - DR is not a direct caller here; treat as background context.
- Q3: Output integrity
  - Stamp/flags/hits artifacts exist.
- Q4: Dominance / noise
  - DR top candidates are dominated by non-winner patterns.
- Q5: Where the winners show up
  - Mostly as contact, not as ranked candidates.
- Q6: Miss analysis
  - DR misses both draws as a caller.
- Q7: Validation checks (V)
  - No missing artifacts indicated.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - None now (DR is background only here).
- Q10: Analyst’s extra insight
  - DR combined-lens presence can be treated as weak corroboration, not primary evidence.

---

### 2.VTRAC Analyzer — SouthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — SouthCarolina4 (stamp 20251223_052418)

## Top indices (from enhanced JSON)
- index 18 | score 38.424625 | features: presence=23.147125, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 27.079640000000005 | features: presence=13.322140000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 8 | score 25.146500000000003 | features: presence=14.909000000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 24.823375 | features: presence=15.065874999999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 23.933915 | features: presence=12.886414999999998, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 6 | score 19.933750000000003 | features: presence=12.796250000000002, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 31 | score 19.718255000000003 | features: presence=12.420755000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 7 | score 18.557387500000004 | features: presence=11.139887500000002, cross_section=0.5, set_echo=0.3, first_hit=0.2666666666666667
- index 2 | score 18.353929166666667 | features: presence=12.8435125, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 17.747300000000003 | features: presence=8.549800000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
534, 153, 541, 345, 341, 531, 134, 135, 524, 175

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 958 | index 14 | file SouthCarolina4_vtrac14_winner_958_20251223_052109.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 314 | index 24 | file SouthCarolina4_vtrac24_winner_314_20251223_052111.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 958 | index 14 rank 2/35 | score 27.079640000000005 | winner_in_index_straights=False | top_index_straights: 534 (14.31), 345 (8.506), 034 (5.42)
- winner 314 | index 24 rank 10/35 | score 17.747300000000003 | winner_in_index_straights=False | top_index_straights: 341 (8.111), 134 (7.238)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winner indices vs brain outputs
  - 958: idx14 rank 2/35 (strong).
  - 314: idx24 rank 10/35 (moderate).
- Q2: 4 hit criteria mapping
  - VTRAC is a primary driver for both draws on this date (especially for 958).
- Q3: Output integrity
  - Enhanced JSON + winner placements exist and are auditable.
- Q4: Dominance / noise
  - Winner idx14 is near-top; treat as highly meaningful. Winner idx24 is mid-pack but still usable.
- Q5: Where the winners show up
  - Both outcomes have credible index placements.
- Q6: Miss analysis
  - None at the index layer; VTRAC supports both (with different strength).
- Q7: Validation checks (V)
  - Winner placements include rank and score ratios/deltas.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Weight “idx rank <= 10” as a meaningful VTRAC condition (both winners satisfy, 958 strongly).
- Q10: Analyst’s extra insight
  - This is the kind of day where index-family coverage could be cost-effective if you choose to act on VTRAC sets.

---

### 2.Hot Zones — SouthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — SouthCarolina4 (2025-06-23)

## Midday winner 958 (canonical 589)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 114
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 314 (canonical 134)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 97
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 237 | vt_triad 334 | score_mean 23.1 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 567 | vt_triad 123 | score_mean 22.622 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 469 | vt_triad 255 | score_mean 21.35 | tags hot16,hot20,hot8,literal_draw,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 278 | vt_triad 334 | score_mean 21.29 | tags hot16,hot20,set1_bonus,vertical2,vt_only_lane,vt_straight
- rank    5 | triad 244 | vt_triad 35 | score_mean 20.612 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_straight
- rank    6 | triad 069 | vt_triad 125 | score_mean 20.349 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 588 | vt_triad 14 | score_mean 19.807 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 124 | vt_triad 235 | score_mean 19.544 | tags hot12,hot16,hot20,hot8,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    9 | triad 118 | vt_triad 24 | score_mean 19.541 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 113 | vt_triad 24 | score_mean 19.392 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Hot Zones places both winners but at deep ranks (958 rank 114; 314 rank 97), not in the top-20 map.
- Q2: 4 hit criteria mapping
  - Hot Zones is corroboration only here (not isolating).
- Q3: Output integrity
  - Top lanes + per-lane + winner_map artifacts exist; winner_map is a top-20 snapshot.
- Q4: Dominance / noise
  - Top lanes are not the winners; treat as broad structure.
- Q5: Where the winners show up
  - Both are present in top lanes but too deep to treat as Hot Zones-led.
- Q6: Miss analysis
  - Hot Zones is not a primary isolator for either draw.
- Q7: Validation checks (V)
  - “Not in winner_map” is expected when best_rank > 20.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Use Hot Zones as corroboration behind VTRAC + Stable when ranks are deep (this day).
- Q10: Analyst’s extra insight
  - Hot Zones supports the “playable but not dominant” narrative; it does not isolate.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Both winners have credible VTRAC placement (idx14 rank 2; idx24 rank 10) and Stable confirmatory presence.
  - Strong cross-variant tagging exists (314 in Midday tags; 958 in Combined tags).
- Conflicts/noise:
  - No substring evidence; Hot Zones ranks are deep; DR does not isolate.
- Aggregator/aux hooks to test next:
  - Explicitly track cross-variant carry as evidence (this is a good example where the winner’s digits are “visible” in other variants).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-23/SouthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — SouthCarolina4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=675, 847, 069, 402, 442
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=069, 442, 968, 237, 029
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=675, 847, 402, 351, 002

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=61 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=22), P2:9 (gap=33), P3:4 (gap=30)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=936 sev=B
- 288: ds=904 sev=B
- 466: ds=823 sev=B
- 238: ds=815 sev=B
- 788: ds=726 sev=B
- 388: ds=717 sev=B
- 228: ds=708 sev=B
- 557: ds=707 sev=B
- 137: ds=688 sev=B
- 668: ds=676 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=88 sev=blue
  - 33: ds=51 sev=purple
  - 99: ds=28 sev=purple
  - 55: ds=25 sev=purple
  - 22: ds=23 sev=-
  - 77: ds=21 sev=-
  - 88: ds=18 sev=-
  - 11: ds=9 sev=-
  - 00: ds=7 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 28: ds=142 sev=red
  - 18: ds=73 sev=red
  - 01: ds=39 sev=blue
  - 17: ds=39 sev=blue
  - 14: ds=38 sev=blue
  - 19: ds=38 sev=blue
  - 08: ds=37 sev=blue
  - 45: ds=35 sev=purple
  - 39: ds=33 sev=purple
  - 34: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 2:188, 1:146, 5:105, 19:95, 34:94, 32:85, 6:84, 4:81, 15:62, 26:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 2:ds=188 fs=9 fl=4 hz=0.016414141414141416, 1:ds=146 fs=5 fl=3 hz=0.011299435028248588, 5:ds=105 fs=21 fl=1 hz=0.028061224489795922, 19:ds=95 fs=13 fl=1 hz=0.016968325791855206, 34:ds=94 fs=26 fl=2 hz=0.031180400890868598, 32:ds=85 fs=2 fl=2 hz=0.005675368898978434, 6:ds=84 fs=21 fl=1 hz=0.02480270574971815, 4:ds=81 fs=26 fl=2 hz=0.03153153153153153, 15:ds=62 fs=13 fl=3 hz=0.01845444059976932, 26:ds=58 fs=2 fl=0 hz=0.007894736842105263

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=94 flags=blue+purple
- S25: ds=83 flags=purple
- S3: ds=60 flags=purple
- S13: ds=48 flags=purple
- S20: ds=46 flags=purple
- S17: ds=43 flags=purple
- S4: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS
  - 049: score=2 tags=RS
  - 058: score=2 tags=RS
  - 067: score=2 tags=RS
  - 247: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=36 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=47), P2:8 (gap=25), P3:1 (gap=27)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 144: ds=976 sev=B
- 777: ds=975 sev=B
- 224: ds=946 sev=B
- 011: ds=766 sev=B
- 277: ds=712 sev=B
- 555: ds=707 sev=B
- 222: ds=684 sev=B
- 048: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=61 sev=purple
  - 00: ds=54 sev=purple
  - 88: ds=41 sev=purple
  - 66: ds=40 sev=purple
  - 33: ds=23 sev=-
  - 99: ds=12 sev=-
  - 55: ds=11 sev=-
  - 22: ds=10 sev=-
  - 77: ds=9 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 78: ds=126 sev=red
  - 04: ds=85 sev=red
  - 28: ds=65 sev=red
  - 08: ds=41 sev=blue
  - 56: ds=37 sev=blue
  - 15: ds=35 sev=purple
  - 35: ds=34 sev=purple
  - 18: ds=33 sev=purple
  - 16: ds=29 sev=purple
  - 67: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:294, 32:248, 1:168, 2:86, 5:85, 16:61, 8:60, 4:54, 34:44, 19:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=294 fs=23 fl=0 hz=0.03412462908011869, 32:ds=248 fs=1 fl=2 hz=0.006993006993006993, 1:ds=168 fs=4 fl=3 hz=0.00963855421686747, 2:ds=86 fs=11 fl=1 hz=0.015435501653803748, 5:ds=85 fs=20 fl=0 hz=0.02531645569620253, 16:ds=61 fs=3 fl=1 hz=0.009191176470588236, 8:ds=60 fs=42 fl=1 hz=0.04767184035476718, 4:ds=54 fs=26 fl=2 hz=0.030871003307607496, 34:ds=44 fs=27 fl=1 hz=0.03083700440528634, 19:ds=43 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=97 flags=blue+purple
- S4: ds=92 flags=purple
- S21: ds=43 flags=purple
- S16: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=73 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=38), P2:9 (gap=18), P3:4 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 114: ds=975 sev=B
- 238: ds=892 sev=B
- 558: ds=870 sev=B
- 477: ds=857 sev=B
- 000: ds=854 sev=B
- 556: ds=820 sev=B
- 115: ds=815 sev=B
- 111: ds=802 sev=B
- 999: ds=787 sev=B
- 078: ds=774 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=114 sev=red
  - 66: ds=84 sev=blue
  - 44: ds=60 sev=purple
  - 22: ds=58 sev=purple
  - 55: ds=32 sev=purple
  - 33: ds=31 sev=purple
  - 99: ds=25 sev=purple
  - 88: ds=10 sev=-
  - 11: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 28: ds=91 sev=red
  - 09: ds=48 sev=blue
  - 18: ds=43 sev=blue
  - 06: ds=40 sev=blue
  - 34: ds=37 sev=blue
  - 46: ds=34 sev=purple
  - 49: ds=34 sev=purple
  - 68: ds=29 sev=purple
  - 23: ds=28 sev=purple
  - 27: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:292, 19:212, 26:205, 6:147, 10:110, 2:107, 1:79, 15:76, 5:57, 14:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=292 fs=3 fl=1 hz=0.017391304347826087, 19:ds=212 fs=16 fl=2 hz=0.02319587628865979, 26:ds=205 fs=0 fl=0 hz=0.002628120893561104, 6:ds=147 fs=23 fl=2 hz=0.030637254901960783, 10:ds=110 fs=20 fl=0 hz=0.024110218140068886, 2:ds=107 fs=13 fl=3 hz=0.01875732708089097, 1:ds=79 fs=2 fl=0 hz=0.005440696409140369, 15:ds=76 fs=23 fl=1 hz=0.028103044496487116, 5:ds=57 fs=16 fl=3 hz=0.0202991452991453, 14:ds=53 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S3: ds=73 flags=purple
- S22: ds=68 flags=purple
- S26: ds=51 flags=blue+purple
- S7: ds=49 flags=purple
- S14: ds=46 flags=purple
- S25: ds=45 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 129: score=1 tags=FLT
  - 139: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 115 -> combined:674(B); evening:815(B)
- 238 -> combined:815(B); evening:892(B)
- 788 -> combined:726(B); evening:759(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:39(blue); midday:27(purple)
- 08 -> combined:37(blue); midday:41(blue)
- 18 -> combined:73(red); evening:43(blue); midday:33(purple)
- 19 -> combined:38(blue); evening:26(purple)
- 28 -> combined:142(red); evening:91(red); midday:65(red)
- 33 -> combined:51(purple); evening:31(purple)
- 34 -> combined:30(purple); evening:37(blue)
- 55 -> combined:25(purple); evening:32(purple)
- 66 -> combined:88(blue); evening:84(blue); midday:40(purple)
- 99 -> combined:28(purple); evening:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.997657142857142)[R1,XVAR-Cons(CEM)], 2(1.7449999999999999)[R1,Double-Pressure], 1(1.7153857142857145)[R3,XVAR-Cons(CM)], 9(1.1806999999999999)[R2,Double-Pressure], 3(1.0344)[R2,Double-Pressure]
- P2: 9(7.159542857142858)[R1,XVAR-Cons(CEM)], 8(6.729285714285715)[R2,XVAR-Cons(CEM)], 3(1.0745714285714285)[R2,Mirror-Echo], 1(1.0553)[R2,Double-Pressure], 2(0.2414285714285714)[R3,Swap]
- P3: 4(8.1397)[R1,XVAR-Cons(CEM)], 3(3.6357999999999997)[R2,XVAR-Cons(CE)], 0(1.8091428571428572)[R3,XVAR-Cons(CE)], 1(1.4061428571428571)[R1,Double-Pressure], 5(0.14779285714285711)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-23 --state SouthCarolina4 --strict` → OK.
- Q2:
  - Positional top digits:
    - Combined: 5/9/4; Midday: 5/8/1; Evening: 2/9/4.
  - These do not isolate 589/134; treat as context.
- Q3:
  - Positional shortlist is broad; use only when it converges with VTRAC/Stable candidates.
- Q4:
  - Repeat watch current_index:
    - Combined=7; Midday=9; Evening=7 (does not match winners’ indices 14/24).
- Q5:
  - VTRAC overdue overlay:
    - Winner idx14 ds is moderate (19 Midday, 53 Evening); winner idx24 is fresh (2 Midday).
    - This does not contradict the strong VTRAC analyzer placement; treat overdue as context only.
- Q6:
  - Due doubles are extreme; not directly isolating winners.
- Q7:
  - Pairs/pairs-remaining are not decisive here.
- Q8:
  - Sums/pairs alerts exist but are low-discrimination.
- Q9:
  - Blackapple is low (Evening score=0); treat as non-decisive.
- Q10:
  - Actionability:
    - Aux is context only; the actionable channels are VTRAC + Stable plus cross-variant tagging in the winners lens.

---

## Part 4 — Combination / Permutation Translation (candidate pack)
Use Part 4 prompts in the master template to produce:
- A small candidate universe per draw (Midday/Evening)
- Evidence vectors per candidate (tools + aux signals)
- Coverage mapping (perm-only vs boxed vs VTRAC-straight vs full index-box)

Reference:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

Part 4 notes / answers:
- Candidate universe (Midday):
  - Primary: `589` box (covers 958) and/or VTRAC idx14 family coverage (8 straights).
- Candidate universe (Evening):
  - Primary: `134` box (covers 314) and/or VTRAC idx24 family coverage (8 straights).
- Evidence vectors:
  - Both: VTRAC idx ranks (2 and 10) + Stable present + strong cross-variant tag density.
- Coverage mapping + pack decision:
  - Keep spend tight: box `589` (Midday) and box `134` (Evening); consider index-family coverage only if you explicitly act on STR8 sets.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday: `589` box would have hit (perm set contains 958).
  - Evening: `134` box would have hit (perm set contains 314).
- Key tags:
  - 314: strong Midday hit-winner tagging (12) despite being Evening winner (cross-variant visibility).
  - 958: strong Combined hit-winner tagging (10) and strong Evening carry (hit-winner-gap=29).
- Drivers:
  - VTRAC index placement is the strongest common driver; Stable is confirmatory.
- Conflicts:
  - No substring evidence; Hot Zones deep; DR not isolating.
- Fix-now vs fix-later:
  - Fix-now: none.
  - Fix-later: none.
- Next run:
  - Proceed to Virginia4 for 2025-06-23.
