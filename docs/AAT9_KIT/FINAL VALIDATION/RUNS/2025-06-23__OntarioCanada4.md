# Master Validation Run Report — OntarioCanada4 — results 2025-06-23 (history workbook ~ 2025-06-22)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-23/OntarioCanada4/`
- Winners lens: `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-06-23/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-06-23/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-06-23/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-06-23/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2025-06-23/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2025-06-23/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_325_20251223_052103.html`
- `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac33_winner_438_20251223_052105.html`

Winners JSON files:
- `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac11_winner_325_20251223_052103.json`
- `sharepacks/2025-06-23/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac33_winner_438_20251223_052105.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are active with a heavy Midday ladder universe and a simpler Evening/Combined ladder structure, but this is not a direct “printed lane equals winner” day; the Evening outcome is mostly narrated by VTRAC-family structure and tags.
  - Winners: Midday=325 (canonical 235); Evening=438 (canonical 348) from `data/results/2025-06-23.txt`.
  - Set1/Draw1 ladders (from winners JSON; lens only, not “outcomes”):
    - Midday: col1 `546** / 564** / 645** / 654**`; col2 `5946** / 5964** / 6594** / 9645**`
    - Evening: col1/col2 `229** / 922**`
    - Combined: col1/col2 `0094** / 9004** / 9400**`
- Q2: Ladder persistence exists, but ladders are not direct winners (235/348); treat ladders as structure and lean on tool ranks + tag density.
- Q3: Winner tagging (from winners JSON):
  - 325 (canon 235): very low hit-winner presence (0) and no substring evidence; mostly gap pressure in Evening.
    - Midday: hit-winner=0; hit-winner-gap=6; hit-family=2; hit-family-gap=22.
    - Evening: hit-winner=0; hit-winner-gap=32; hit-family=10; hit-family-gap=52.
    - Combined: hit-winner=0; hit-winner-gap=4; hit-family=6; hit-family-gap=24.
  - 438 (canon 348): stronger family and vt-straight tagging, with some Combined hit-winner tags.
    - Midday: hit-winner=0; hit-winner-gap=3; hit-family=48; hit-family-gap=53; hit-vt-straight=14.
    - Evening: hit-winner=0; hit-winner-gap=8; hit-family=70; hit-family-gap=70; hit-vt-straight=15.
    - Combined: hit-winner=3; hit-winner-gap=7; hit-family=33; hit-family-gap=33; hit-vt-straight=8.
- Q4: Variant bias:
  - 438 is the more coherent environment (VTRAC support + vt-straight tagging).
  - 325 is weak across on-board metrics (no hit-winner tags, no substring evidence).
- Q5: Permutation lane clarity:
  - 438: higher at the VTRAC layer (idx33 is top-3).
  - 325: low (weak tool support and low tag density).
- Q6: Environment verdict: **Evening playable; Midday very cautious**
  - Evening 438: VTRAC idx33 rank 3/35 is strong support, with moderate Hot Zones placement (rank 46).
  - Midday 325: Stable misses as a canonical isolate and VTRAC rank is deep (idx11 rank 32/35); Hot Zones is weak (rank 143).
- Q7: Hot Zones overlap:
  - 325 best rank 143 (weak).
  - 438 best rank 46 (moderate).
- Q8: Cross-set carryover:
  - 438 shows some Combined hit-winner tags and strong family/vt-straight tagging across variants.
  - 325 does not show a strong carry signature.
- Q9: Aux cues (quick lens):
  - Repeat watch current_index (Combined=16, Midday=24, Evening=16) does not match winners’ indices (11/33).
  - BA is moderate (Combined score=3; Midday/Evening score=2) but not decisive by itself.
- Q10: 4 hit criteria viability (pre-results lens):
  - Evening: VTRAC is the clear leader (idx33 top-3) with Hot Zones as corroboration.
  - Midday: no strong leader (Stable misses; VTRAC deep; Hot Zones weak; DR not isolating).
- Q11: Exact triple presence (winners lens):
  - Literal/canonical substring cells are 0 for both winners; interpret via tags + tool evidence.
- Q12: “Profitable environment” summary:
  - This is a one-sided day: one draw is VTRAC-supported (Evening), the other is largely diffuse (Midday).
- Q13: Dominance vs dilution:
  - Avoid over-weighting the Midday ladder universe; it is structured but not predictive of 235.
- Q14: Noise check:
  - High for Midday; moderate for Evening.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — OntarioCanada4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2025-06-23)

## Midday winner 325 (canonical 235)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=51 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 11 rows contain digits; best rank 1093, section Combined, score 9.0, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=13
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 438 (canonical 348)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=3 | family_rows=183 | exact_boxed=3 | exact_straight=3 | vt_boxed=3
- Scores (patterns_scores.csv): rank 4718, section Combined, Set Set1, Draw Draw1, Col 7, score 9.5, hot 0, vt_straight 0.0 | why straight|cov1|hp_repeat2|mirror|hidden3v|draw_chain2
- Compound (patterns_compound.csv): rank 1262, section Combined, score 10.5, col1_hits 0, hot2 0, set_chain 1, draw_chain 2 | why draw_chain2
- Families (patterns_families.csv): 45 rows contain digits; best rank 84, section Evening, score 27.5, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=22

## Top compound candidates (patterns_compound.csv)
- rank    5 | canon 004 | section Combined | score 84.5 | col1_hits 7 | hot2 11
- rank   11 | canon 456 | section Midday | score 65.5 | col1_hits 5 | hot2 11
- rank    2 | canon 009 | section Combined | score 93.5 | col1_hits 9 | hot2 11
- rank    1 | canon 229 | section Evening | score 108.0 | col1_hits 9 | hot2 11
- rank    7 | canon 0049 | section Combined | score 72.5 | col1_hits 5 | hot2 9
- rank    8 | canon 0059 | section Combined | score 68.5 | col1_hits 6 | hot2 8
- rank    4 | canon 005 | section Combined | score 88.5 | col1_hits 6 | hot2 8
- rank    9 | canon 059 | section Combined | score 67.5 | col1_hits 6 | hot2 8
- rank   15 | canon 346 | section Midday | score 57.0 | col1_hits 5 | hot2 8
- rank   87 | canon 029 | section Evening | score 35.0 | col1_hits 3 | hot2 6

## Top families (patterns_families.csv)
- rank 1256 | family 3 | score 5.5 | hot2 0 | section Midday
- rank 1143 | family 34 | score 8.0 | hot2 0 | section Midday
- rank  372 | family 14 | score 19.5 | hot2 0 | section Midday
- rank  372 | family 24 | score 19.5 | hot2 0 | section Midday
- rank  411 | family 9 | score 19.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday 325: winner canonical 235 is missing from Stable scores and compound (gaps: missing_from_scores, missing_from_compound).
  - Evening 438: present but extremely deep (scores rank 4718; compound rank 1262).
- Q2: 4 hit criteria mapping
  - Stable is not a usable driver for either draw on this date (Midday miss; Evening very deep).
- Q3: Output integrity
  - Stable artifacts exist; gaps reflect tool outcome (winner not isolated), not missing files.
- Q4: Dominance / noise
  - Stable top compound candidates are not aligned to either winner canonical.
- Q5: Where the winners show up
  - 325: not in scores/compound; only appears in family/metrics layers.
  - 438: deep in scores/compound.
- Q6: Miss analysis
  - Stable misses both draws as an isolator; do not weight Stable heavily for Ontario on this date.
- Q7: Validation checks (V)
  - Treat “missing_from_scores/compound” as tool outcome, not pipeline failure.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Use VTRAC/Hot Zones to lead Evening; Stable should not be leading.
- Q10: Analyst’s extra insight
  - This is a good case for the “no single tool must lead every draw” principle.

---

### 2.Digit Reduction — OntarioCanada4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20251223)

## Midday winner 325 (canonical 235)
- Stamp (winner_stamp.json): items_total=30 | exact_any=0 exact_final=0 | vtrac_any=23 vtrac_final=0 | drop_exact_any=2 drop_exact_final=0 | drop_vtrac_any=12 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=30 | exact_any=0 vtrac_any=23 | drop_exact_any=2 drop_vtrac_any=12 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=30 vt_straight=0
- Hits (winner_hits.csv): rows=30 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=30 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 438 (canonical 348)
- Stamp (winner_stamp.json): items_total=147 | exact_any=0 exact_final=0 | vtrac_any=147 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=20 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=147 | exact_any=0 vtrac_any=147 | drop_exact_any=0 drop_vtrac_any=20 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=33 vt_straight=0
- Hits (winner_hits.csv): rows=147 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=33 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 325 (canonical 235)
- Stamp (winner_stamp.json): items_total=73 | exact_any=0 exact_final=0 | vtrac_any=52 vtrac_final=0 | drop_exact_any=9 drop_exact_final=0 | drop_vtrac_any=24 drop_vtrac_final=0 | family_exact_any=9 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=73 | exact_any=0 vtrac_any=52 | drop_exact_any=9 drop_vtrac_any=24 | family_exact_any=9 family_vtrac_any=3 | vt_boxed=69 vt_straight=0
- Hits (winner_hits.csv): rows=73 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=69 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 4 | pattern 599 | score_v2 12.937143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 12.577143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 5 | pattern 592 | score_v2 12.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 4 | pattern 592 | score_v2 12.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 5 | pattern 599 | score_v2 12.408571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 7 | pattern 599 | score_v2 12.370476 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw1 col 6 | pattern 599 | score_v2 12.370476 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 12.327143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 599 | score_v2 12.237143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 3 | pattern 592 | score_v2 12.177143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 12.937143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 559 | score_v2 12.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 592 | score_v2 12.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 922 | score_v2 12.064643 | tags exact,vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 559 | score_v2 11.737143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 599 | score_v2 11.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 592 | score_v2 11.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 559 | score_v2 11.670476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 11.497143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 992 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR shows contact but does not promote either winner into top candidates (winner_present=False across variants).
- Q2: 4 hit criteria mapping
  - DR is not actionable here; treat as context only.
- Q3: Output integrity
  - Stamp/flags/hits artifacts exist.
- Q4: Dominance / noise
  - Top candidates are dominated by other patterns, not 235/348.
- Q5: Where the winners show up
  - Only as broad contact, not as ranked candidates.
- Q6: Miss analysis
  - DR misses both outcomes as a caller.
- Q7: Validation checks (V)
  - No missing artifacts indicated.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - None now (DR is background only here).
- Q10: Analyst’s extra insight
  - This state/day reinforces DR’s role as pressure/context, not isolation.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20251223_052415)

## Top indices (from enhanced JSON)
- index 5 | score 83.91228499999995 | features: presence=61.20478499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 83.31800999999996 | features: presence=60.66050999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 35.9823 | features: presence=20.9948, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 34 | score 31.810100000000006 | features: presence=17.872600000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 25 | score 27.286950000000004 | features: presence=16.629450000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 9 | score 24.321550000000002 | features: presence=16.044050000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 22.213370000000005 | features: presence=11.495870000000004, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 35 | score 22.061812500000002 | features: presence=11.894312500000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 19 | score 19.525750000000002 | features: presence=12.938250000000002, cross_section=0.5, set_echo=0.3, first_hit=0.2666666666666667
- index 22 | score 18.712700000000005 | features: presence=12.275200000000003, set_echo=0.3, first_hit=0.33333333333333337, column_span=0.25416666666666665

## Top straights (from enhanced JSON)
594, 094, 940, 059, 590, 095, 945, 934, 593, 943

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 325 | index 11 | file OntarioCanada4_vtrac11_winner_325_20251223_052103.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 438 | index 33 | file OntarioCanada4_vtrac33_winner_438_20251223_052105.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 325 | index 11 rank 32/35 | score 0.5918749999999999 | winner_in_index_straights=False | top_index_straights: 875 (0.09)
- winner 438 | index 33 rank 3/35 | score 35.9823 | winner_in_index_straights=False | top_index_straights: 983 (9.83), 834 (9.306)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winner indices vs brain outputs
  - 438: idx33 rank 3/35 (strong placement).
  - 325: idx11 rank 32/35 (very weak placement).
- Q2: 4 hit criteria mapping
  - VTRAC supports Evening strongly (idx33 top-3); it does not support Midday.
- Q3: Output integrity
  - Enhanced JSON + winner placements exist and are auditable.
- Q4: Dominance / noise
  - Winner idx33 is not the top index, but it is still highly ranked (strong enough to act on).
- Q5: Where the winners show up
  - 438 shows up as a top-3 index; 325 does not.
- Q6: Miss analysis
  - VTRAC misses Midday as an isolator; supports Evening.
- Q7: Validation checks (V)
  - Winner index rank/score deltas are present.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Treat “VTRAC top-5 index placement” as a high-value channel (Evening here).
- Q10: Analyst’s extra insight
  - When VTRAC is strong and Stable is weak, let VTRAC lead the candidate universe.

---

### 2.Hot Zones — OntarioCanada4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2025-06-23)

## Midday winner 325 (canonical 235)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 143
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 438 (canonical 348)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 46
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 166 | vt_triad 22 | score_mean 21.848 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    2 | triad 157 | vt_triad 123 | score_mean 21.607 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_straight
- rank    3 | triad 112 | vt_triad 23 | score_mean 21.354 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    4 | triad 678 | vt_triad 234 | score_mean 21.329 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 266 | vt_triad 23 | score_mean 21.008 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical1,vertical3,vt_straight
- rank    6 | triad 227 | vt_triad 33 | score_mean 20.75 | tags funnel_precol1,hot16,ls_col_42,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 267 | vt_triad 233 | score_mean 20.705 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    8 | triad 277 | vt_triad 33 | score_mean 20.69 | tags funnel_precol1,hot16,ls_col_42,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 368 | vt_triad 244 | score_mean 20.461 | tags funnel_precol1,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical2,vertical3,vertical4,vt_straight
- rank   10 | triad 127 | vt_triad 233 | score_mean 20.435 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - 438: top lanes best rank 46 (moderate) with straight/vt-straight lane support.
  - 325: top lanes best rank 143 (weak) with no straight lane and only vt-straight lane support.
- Q2: 4 hit criteria mapping
  - Hot Zones is usable as corroboration for Evening (rank 46), not for Midday.
- Q3: Output integrity
  - Top lanes + per-lane + winner_map artifacts exist; winner_map is a top-20 snapshot.
- Q4: Dominance / noise
  - Top lanes are not winners; treat as broad-lane structure.
- Q5: Where the winners show up
  - 438 is moderately placed (rank 46); 325 is deep.
- Q6: Miss analysis
  - Hot Zones misses Midday; it provides modest support for Evening.
- Q7: Validation checks (V)
  - “Not in winner_map” is expected when best_rank > 20.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Use Hot Zones as corroboration behind VTRAC for Evening when Stable is weak.
- Q10: Analyst’s extra insight
  - This state/day is VTRAC-led; Hot Zones is secondary.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Evening 438 is the only coherent convergence: VTRAC idx33 top-3 plus strong family/vt-straight tagging.
- Conflicts/noise:
  - Stable is weak (Midday miss; Evening very deep), DR does not isolate, and Hot Zones is only moderate for Evening.
- Aggregator/aux hooks to test next:
  - Keep “VTRAC top-5 index placement” as a high-priority channel even when Stable is weak.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-23/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=616, 918, 517, 678, 343
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=918, 678, 211, 221, 847
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=616, 517, 343, 367, 875

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=3 last_repeat_gap=41 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:8 (gap=32), P3:2 (gap=38)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 004: ds=837 sev=B
- 288: ds=830 sev=B
- 778: ds=811 sev=B
- 115: ds=804 sev=B
- 144: ds=795 sev=B
- 055: ds=773 sev=B
- 346: ds=747 sev=B
- 255: ds=730 sev=B
- 111: ds=720 sev=B
- 116: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=123 sev=red
  - 00: ds=95 sev=blue
  - 55: ds=76 sev=blue
  - 77: ds=46 sev=purple
  - 99: ds=27 sev=purple
  - 44: ds=21 sev=-
  - 22: ds=7 sev=-
  - 11: ds=5 sev=-
  - 33: ds=4 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 35: ds=67 sev=red
  - 59: ds=58 sev=red
  - 26: ds=49 sev=blue
  - 24: ds=48 sev=blue
  - 25: ds=45 sev=blue
  - 79: ds=39 sev=blue
  - 27: ds=34 sev=purple
  - 39: ds=29 sev=purple
  - 02: ds=28 sev=purple
  - 29: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:691, 1:287, 6:119, 26:118, 13:112, 5:84, 34:62, 28:61, 3:45, 10:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=691 fs=0 fl=0 hz=0.0, 1:ds=287 fs=1 fl=1 hz=0.006172839506172839, 6:ds=119 fs=10 fl=4 hz=0.016726403823178016, 26:ds=118 fs=3 fl=2 hz=0.008174386920980927, 13:ds=112 fs=22 fl=0 hz=0.02631578947368421, 5:ds=84 fs=28 fl=0 hz=0.03571428571428571, 34:ds=62 fs=12 fl=4 hz=0.017185821697099892, 28:ds=61 fs=17 fl=2 hz=0.020255863539445626, 3:ds=45 fs=20 fl=1 hz=0.022629310344827586, 10:ds=38 fs=24 fl=2 hz=0.02774813233724653

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=98 flags=blue+purple
- S22: ds=58 flags=purple
- S6: ds=54 flags=red+purple
- S7: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': True}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=3 tags=FLT,MIR,PAT
  - 016: score=3 tags=FLT,MIR,PAT
  - 025: score=3 tags=FLT,MIR,PAT
  - 027: score=3 tags=FLT,MIR,PAT
  - 035: score=3 tags=FLT,MIR,PAT
  - 038: score=3 tags=FLT,MIR,PAT
  - 045: score=3 tags=FLT,MIR,PAT
  - 049: score=3 tags=FLT,MIR,PAT
  - 126: score=3 tags=FLT,MIR,PAT
  - 127: score=3 tags=FLT,MIR,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=21 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=19), P2:8 (gap=25), P3:6 (gap=26)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=955 sev=B
- 099: ds=905 sev=B
- 228: ds=802 sev=B
- 333: ds=785 sev=B
- 255: ds=752 sev=B
- 566: ds=728 sev=B
- 338: ds=722 sev=B
- 355: ds=717 sev=B
- 011: ds=695 sev=B
- 368: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=109 sev=red
  - 88: ds=61 sev=purple
  - 66: ds=59 sev=purple
  - 00: ds=47 sev=purple
  - 55: ds=43 sev=purple
  - 77: ds=30 sev=purple
  - 99: ds=13 sev=-
  - 44: ds=10 sev=-
  - 22: ds=3 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 17: ds=48 sev=blue
  - 57: ds=46 sev=blue
  - 59: ds=43 sev=blue
  - 37: ds=40 sev=blue
  - 16: ds=36 sev=purple
  - 34: ds=34 sev=purple
  - 23: ds=33 sev=purple
  - 35: ds=33 sev=purple
  - 27: ds=32 sev=purple
  - 24: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:345, 16:187, 1:143, 34:128, 27:104, 26:91, 10:73, 33:64, 13:61, 6:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=345 fs=1 fl=1 hz=0.0056603773584905665, 16:ds=187 fs=4 fl=0 hz=0.008450704225352114, 1:ds=143 fs=4 fl=2 hz=0.011976047904191617, 34:ds=128 fs=13 fl=3 hz=0.01909307875894988, 27:ds=104 fs=16 fl=2 hz=0.020202020202020204, 26:ds=91 fs=0 fl=4 hz=0.006150061500615006, 10:ds=73 fs=22 fl=1 hz=0.02561247216035635, 33:ds=64 fs=22 fl=1 hz=0.026047565118912798, 13:ds=61 fs=21 fl=3 hz=0.026402640264026403, 6:ds=59 fs=18 fl=1 hz=0.02065217391304348

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=96 flags=blue+purple
- S3: ds=88 flags=purple
- S6: ds=75 flags=red+purple
- S2: ds=71 flags=purple
- S9: ds=47 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=3 tags=FLT,RS
  - 024: score=3 tags=FLT,RS
  - 069: score=3 tags=FLT,RS
  - 078: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 159: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 348: score=3 tags=FLT,RS
  - 357: score=3 tags=FLT,RS
  - 456: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=3 last_repeat_gap=25 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:3 (gap=30), P3:9 (gap=25)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=986 sev=B
- 228: ds=932 sev=B
- 337: ds=899 sev=B
- 145: ds=854 sev=B
- 016: ds=835 sev=B
- 066: ds=832 sev=B
- 777: ds=820 sev=B
- 388: ds=806 sev=B
- 588: ds=773 sev=B
- 227: ds=721 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=90 sev=blue
  - 11: ds=51 sev=purple
  - 00: ds=49 sev=purple
  - 55: ds=38 sev=purple
  - 22: ds=28 sev=purple
  - 99: ds=25 sev=purple
  - 77: ds=23 sev=-
  - 44: ds=15 sev=-
  - 33: ds=2 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 12: ds=108 sev=red
  - 26: ds=68 sev=red
  - 35: ds=38 sev=blue
  - 06: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 39: ds=31 sev=purple
  - 59: ds=29 sev=purple
  - 25: ds=28 sev=purple
  - 05: ds=27 sev=purple
  - 79: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:676, 35:234, 6:197, 28:169, 1:149, 20:119, 3:116, 17:102, 26:59, 13:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=676 fs=1 fl=2 hz=0.009433962264150943, 35:ds=234 fs=0 fl=3 hz=0.005657708628005658, 6:ds=197 fs=14 fl=2 hz=0.02077922077922078, 28:ds=169 fs=7 fl=0 hz=0.011335012594458438, 1:ds=149 fs=0 fl=0 hz=0.0, 20:ds=119 fs=18 fl=1 hz=0.02280912364945978, 3:ds=116 fs=16 fl=3 hz=0.023199023199023196, 17:ds=102 fs=17 fl=3 hz=0.022753128555176336, 26:ds=59 fs=3 fl=2 hz=0.007552870090634441, 13:ds=56 fs=23 fl=2 hz=0.02969121140142518

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S25: ds=90 flags=purple
- S27: ds=80 flags=blue+purple
- S19: ds=78 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 228 -> evening:932(B); midday:802(B)
- 255 -> combined:730(B); midday:752(B)
- 288 -> combined:830(B); midday:955(B)
- 338 -> evening:676(B); midday:722(B)
- 388 -> combined:691(B); evening:806(B)
- 778 -> combined:811(B); evening:986(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:95(blue); evening:49(purple); midday:47(purple)
- 24 -> combined:48(blue); midday:31(purple)
- 25 -> combined:45(blue); evening:28(purple)
- 26 -> combined:49(blue); evening:68(red)
- 27 -> combined:34(purple); midday:32(purple)
- 35 -> combined:67(red); evening:38(blue); midday:33(purple)
- 39 -> combined:29(purple); evening:31(purple)
- 55 -> combined:76(blue); evening:38(purple); midday:43(purple)
- 59 -> combined:58(red); evening:29(purple); midday:43(blue)
- 77 -> combined:46(purple); midday:30(purple)
- 79 -> combined:39(blue); evening:26(purple)
- 88 -> combined:123(red); evening:90(blue); midday:61(purple)
- 99 -> combined:27(purple); evening:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.382042857142857)[R2,XVAR-Cons(CEM)], 4(4.703892857142857)[R3,XVAR-Cons(CEM)], 7(3.8215714285714286)[R1,XVAR-Cons(CM)], 9(1.0678071428571427)[R2,Mirror-Echo]
- P2: 5(6.8957)[R2,XVAR-Cons(CEM)], 8(6.510685714285715)[R1,Mirror-Echo], 3(3.1627142857142854)[R3,Mirror-Echo], 6(0.19092142857142858)[R3,Swap]
- P3: 2(7.7196)[R1,XVAR-Cons(CEM)], 9(4.067035714285714)[R2,Mirror-Echo], 4(2.4078214285714283)[R3,Mirror-Echo], 6(1.3762857142857143)[R1,Double-Pressure], 3(0.2881)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-23 --state OntarioCanada4 --strict` → OK.
- Q2:
  - Positional top digits:
    - Combined: 7/8/2; Midday: 7/8/6; Evening: 1/3/9.
  - These do not isolate 235/348; treat as context only.
- Q3:
  - Positional shortlist is broad; use only if it converges with VTRAC-led candidates (Evening).
- Q4:
  - Repeat watch current_index:
    - Combined=16; Midday=24; Evening=16 (does not match winners’ indices 11/33).
- Q5:
  - VTRAC overdue overlay:
    - Winner idx33 is fresh (ds=2 Evening); winner idx11 is modestly due (ds=25 Midday), but VTRAC ranking is still deep for idx11.
- Q6:
  - Due doubles are extreme (e.g., Combined 004 ds=837), but do not isolate 235/348.
- Q7:
  - Pairs/pairs-remaining are not decisive on this date.
- Q8:
  - Sums/pairs alerts exist but are low-discrimination.
- Q9:
  - Blackapple is moderate (Combined score=3), but not decisive by itself.
- Q10:
  - Actionability:
    - Aux is context only; the actionable channel is Evening VTRAC (idx33) with Hot Zones corroboration.

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
  - No strong isolate; if forced, a cautious `235` box (covers 325) should require corroboration.
- Candidate universe (Evening):
  - Primary: `348` box/straight and/or VTRAC idx33 family coverage (8 straights), since idx33 is top-3.
- Evidence vectors:
  - Evening: VTRAC idx33 top-3 + vt-straight tagging + Hot Zones moderate placement.
  - Midday: weak across tools; avoid unless corroborated.
- Coverage mapping + pack decision:
  - Keep spend tight: act on Evening (box `348`); avoid Midday unless additional evidence emerges.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Evening: `348` box/straight would have hit (perm set contains 438).
  - Midday: `235` box would have hit (perm set contains 325) but evidence was weak.
- Key tags:
  - 438: strong hit-family + hit-vt-straight tagging across variants.
  - 325: low hit-winner tags; mostly gap pressure.
- Drivers:
  - Evening win is driven by VTRAC idx33 placement; Stable is not a driver here.
- Conflicts:
  - Midday is diffuse: Stable miss + VTRAC deep + Hot Zones deep.
- Fix-now vs fix-later:
  - Fix-now: none.
  - Fix-later: none (collect more Ontario examples before tuning).
- Next run:
  - Proceed to PuertoRico4 for 2025-06-23.
