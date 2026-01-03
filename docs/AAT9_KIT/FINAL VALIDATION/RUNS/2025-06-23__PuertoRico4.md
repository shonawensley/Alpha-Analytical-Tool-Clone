# Master Validation Run Report — PuertoRico4 — results 2025-06-23 (history workbook ~ 2025-06-22)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-23/PuertoRico4/`
- Winners lens: `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2025-06-23/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2025-06-23/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2025-06-23/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2025-06-23/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2025-06-23/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2025-06-23/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac13_winner_858_20251223_052108.html`
- `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac15_winner_454_20251223_052109.html`

Winners JSON files:
- `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac13_winner_858_20251223_052108.json`
- `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac15_winner_454_20251223_052109.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are active but do not directly resolve as the winners; the Evening draw has the clearest on-board evidence via tags + canonical substring, while Midday is weak across the board.
  - Winners: Midday=858 (canonical 588); Evening=454 (canonical 445) from `data/results/2025-06-23.txt`.
  - Set1/Draw1 ladders (from winners JSON; lens only, not “outcomes”):
    - Midday: col1/col2 `003**`
    - Evening: col1/col2 `2900447** / 7009244** / 9244007**`
    - Combined: col1/col2 `2047** / 2407** / 7024**`
- Q2: Ladder strings are coherent but not direct winners (588/445); treat ladders as structure only and prioritize tags + tool evidence.
- Q3: Winner tagging (from winners JSON):
  - 858 (canon 588): no hit-winner tagging; only family/gap pressure and some vt-straight tagging in Evening.
    - Midday: hit-winner=0; hit-winner-gap=0; hit-family=33; hit-family-gap=60.
    - Evening: hit-winner=0; hit-winner-gap=0; hit-family=17; hit-family-gap=30; hit-vt-straight=10.
    - Combined: hit-winner=0; hit-winner-gap=0; hit-family=15; hit-family-gap=29; hit-vt-straight=2.
  - 454 (canon 445): strong Evening on-board evidence, including very high vt-straight tagging and canonical substring presence.
    - Midday: hit-winner=1; hit-winner-gap=1; hit-family=10; hit-family-gap=16; canonical substring cells for `445`=1.
    - Evening: hit-winner=9; hit-winner-gap=9; hit-family=75; hit-family-gap=128; hit-vt-straight=68; canonical substring cells for `445`=9.
    - Combined: hit-winner=2; hit-winner-gap=2; hit-family=26; hit-family-gap=37; hit-vt-straight=10; canonical substring cells for `445`=2.
- Q4: Variant bias:
  - 454 is strongly Evening-driven (tags + substring support).
  - 858 shows mostly family pressure and does not show hit-winner tags on this day.
- Q5: Permutation lane clarity:
  - 454: high (dense tags + substring evidence + convergent tool support).
  - 858: low (no hit-winner tags, weak tool support).
- Q6: Environment verdict: **Evening playable; Midday very cautious**
  - Evening 454 has Stable presence (compound rank 115) plus VTRAC support (idx15 rank 6/35) and strong winners-lens evidence.
  - Midday 858 is weak: Stable misses it as a canonical isolate and VTRAC index placement is mediocre (idx13 rank 20/35 with score 0.0).
- Q7: Hot Zones overlap:
  - 858 best rank 207 (very weak).
  - 454 best rank 119 (weak).
- Q8: Cross-set carryover:
  - 454 shows meaningful Combined carry (vt-straight tags=10; canonical substring=2).
  - 858 carry is weak and mostly family/gap.
- Q9: Aux cues (quick lens):
  - Repeat watch current_index (Combined=2, Midday=9, Evening=2) does not match winners’ indices (13/15).
  - BA is low (score=1 across variants); treat as non-decisive.
- Q10: 4 hit criteria viability (pre-results lens):
  - Evening: strongest evidence is winners-lens tagging + VTRAC idx15 support + Stable presence.
  - Midday: no strong channel (Stable miss + Hot Zones deep).
  - DR does not isolate winners as top candidates.
- Q11: Exact triple presence (winners lens):
  - 454: canonical substring evidence exists (Evening=9; Combined=2; Midday=1).
  - 858: literal/canonical substring cells are 0.
- Q12: “Profitable environment” summary:
  - This is a one-sided day: Evening has convergence; Midday is diffuse/low-signal.
- Q13: Dominance vs dilution:
  - Avoid over-weighting the large Evening ladder strings; the predictive power here is more clearly in tags + tool ranks.
- Q14: Noise check:
  - High for Midday; moderate for Evening.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — PuertoRico4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2025-06-23)

## Midday winner 858 (canonical 588)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=51 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 32 rows contain digits; best rank 108, section Midday, score 28.5, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=9
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 454 (canonical 445)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=97 | exact_boxed=12 | exact_straight=12 | vt_boxed=12
- Scores (patterns_scores.csv): rank 1264, section Evening, Set Set1, Draw Draw5, Col 2, score 17.5, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat2|hot2|hidden3v|double_mirror|vtrac_straight|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 115, section Evening, score 31.0, col1_hits 0, hot2 1, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|hot2x1|vstrx3|dblmirrorx9
- Families (patterns_families.csv): 66 rows contain digits; best rank 7, section Evening, score 34.5, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=7

## Top compound candidates (patterns_compound.csv)
- rank    7 | canon 0244 | section Evening | score 89.0 | col1_hits 9 | hot2 11
- rank    6 | canon 00244 | section Evening | score 89.5 | col1_hits 9 | hot2 11
- rank   13 | canon 249 | section Evening | score 74.0 | col1_hits 6 | hot2 11
- rank   20 | canon 002449 | section Evening | score 66.0 | col1_hits 6 | hot2 11
- rank    1 | canon 244 | section Evening | score 114.5 | col1_hits 9 | hot2 11
- rank    8 | canon 0044 | section Evening | score 86.0 | col1_hits 9 | hot2 11
- rank    2 | canon 447 | section Evening | score 102.0 | col1_hits 9 | hot2 11
- rank    3 | canon 007 | section Evening | score 100.0 | col1_hits 9 | hot2 11
- rank    4 | canon 004 | section Evening | score 96.0 | col1_hits 9 | hot2 11
- rank   10 | canon 009 | section Evening | score 77.5 | col1_hits 7 | hot2 11

## Top families (patterns_families.csv)
- rank 1350 | family 25 | score 4.0 | hot2 0 | section Midday
- rank  992 | family 23 | score 12.5 | hot2 0 | section Midday
- rank 1010 | family 7 | score 12.0 | hot2 0 | section Midday
- rank 1189 | family 22 | score 9.5 | hot2 0 | section Midday
- rank 1287 | family 21 | score 7.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday 858: winner canonical 588 is missing from Stable scores and compound (gaps: missing_from_scores, missing_from_compound).
  - Evening 454: present (scores rank 1264; compound rank 115).
- Q2: 4 hit criteria mapping
  - Stable is usable as a weak-to-moderate corroborator for Evening only; it is not usable for Midday on this date.
- Q3: Output integrity
  - Stable artifacts exist; gaps reflect tool outcome, not missing files.
- Q4: Dominance / noise
  - Stable top candidates are not aligned to 588/445.
- Q5: Where the winners show up
  - 454 is present (moderate compound rank); 858 is not present in scores/compound.
- Q6: Miss analysis
  - Stable misses Midday; partial support for Evening.
- Q7: Validation checks (V)
  - Treat winner absence as tool outcome, not pipeline corruption.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Combine VTRAC index support + winners-lens tag density as the primary driver when Hot Zones is weak.
- Q10: Analyst’s extra insight
  - Puerto Rico on this day is “Evening only”: do not force Midday plays from weak evidence.

---

### 2.Digit Reduction — PuertoRico4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp 20251223)

## Midday winner 858 (canonical 588)
- Stamp (winner_stamp.json): items_total=82 | exact_any=0 exact_final=0 | vtrac_any=80 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=6 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=82 | exact_any=0 vtrac_any=80 | drop_exact_any=0 drop_vtrac_any=6 | family_exact_any=0 family_vtrac_any=2 | vt_boxed=10 vt_straight=0
- Hits (winner_hits.csv): rows=82 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=10 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 454 (canonical 445)
- Stamp (winner_stamp.json): items_total=372 | exact_any=0 exact_final=0 | vtrac_any=372 vtrac_final=31 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=99 drop_vtrac_final=31 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=42 family_vtrac_final=31
- Flags (winner_flags.csv): rows=372 | exact_any=0 vtrac_any=372 | drop_exact_any=0 drop_vtrac_any=99 | family_exact_any=0 family_vtrac_any=42 | vt_boxed=33 vt_straight=31
- Hits (winner_hits.csv): rows=372 | exact_final=0 vtrac_final=31 | drop_exact_final=0 drop_vtrac_final=31 | family_exact_final=0 family_vtrac_final=31 | vt_boxed=33 vt_straight=31
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 551 (canonical 155)
- Stamp (winner_stamp.json): items_total=241 | exact_any=0 exact_final=0 | vtrac_any=241 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=24 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=241 | exact_any=0 vtrac_any=241 | drop_exact_any=0 drop_vtrac_any=24 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=241 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 19.077143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 224 | score_v2 18.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 18.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 244 | score_v2 18.177143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 224 | score_v2 17.977143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 224 | score_v2 14.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 224 | score_v2 14.127143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 224 | score_v2 14.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 224 | score_v2 13.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 924 | score_v2 13.677143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 19.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 244 | score_v2 18.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 224 | score_v2 14.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 924 | score_v2 13.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 244 | score_v2 13.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 924 | score_v2 13.277143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 224 | score_v2 12.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 224 | score_v2 12.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 992 | score_v2 12.087143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 244 | score_v2 12.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR shows high contact but does not promote 858/454 into top candidates (winner_present=False for Midday/Evening).
  - Note: the DR Combined section for this state/date is tagged against a non-results triple (551); treat Combined as a lens only and focus evaluation on Midday/Evening winners.
- Q2: 4 hit criteria mapping
  - DR is not actionable as a direct caller on this state/day.
- Q3: Output integrity
  - Stamp/flags/hits artifacts exist; Midday and Evening overlays correctly use 858 and 454.
- Q4: Dominance / noise
  - Reducer top candidates are not aligned to 588/445.
- Q5: Where the winners show up
  - Only as contact flags, not as ranked candidates.
- Q6: Miss analysis
  - DR misses both outcomes as a caller.
- Q7: Validation checks (V)
  - No missing artifacts indicated.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - None now (DR is background only here).
- Q10: Analyst’s extra insight
  - Record the Combined-winner mismatch as a fix-later item, but it does not block template filling for Midday/Evening.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20251223_052417)

## Top indices (from enhanced JSON)
- index 12 | score 111.93899249999994 | features: presence=80.36149249999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 91.01624249999993 | features: presence=64.42874249999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 31 | score 76.47464999999993 | features: presence=55.49714999999994, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 65.72369249999997 | features: presence=47.27619249999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 47.82124999999999 | features: presence=29.513749999999995, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 15 | score 37.02654999999999 | features: presence=24.819049999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 25.789275 | features: presence=16.181775, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 14 | score 22.113675 | features: presence=9.626175, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 28 | score 20.510875000000002 | features: presence=13.523375000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 11 | score 15.040375000000001 | features: presence=5.772875000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
024, 240, 092, 047, 204, 924, 407, 290, 524, 245

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 858 | index 13 | file PuertoRico4_vtrac13_winner_858_20251223_052108.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 454 | index 15 | file PuertoRico4_vtrac15_winner_454_20251223_052109.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 858 | index 13 rank 20/35 | score 0.0 | winner_in_index_straights=False | top_index_straights: (none)
- winner 454 | index 15 rank 6/35 | score 37.02654999999999 | winner_in_index_straights=False | top_index_straights: 940 (7.488), 094 (6.4), 904 (6.31)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winner indices vs brain outputs
  - 454: idx15 rank 6/35 (usable placement).
  - 858: idx13 rank 20/35 with score 0.0 (weak placement).
- Q2: 4 hit criteria mapping
  - VTRAC is a valid corroborator for Evening; it is not supportive for Midday on this date.
- Q3: Output integrity
  - Enhanced JSON + winner placements exist and are auditable.
- Q4: Dominance / noise
  - Winner idx15 is not the top index but is inside top-6; treat as meaningful.
- Q5: Where the winners show up
  - 454 is elevated at the index layer; 858 is not.
- Q6: Miss analysis
  - VTRAC misses Midday; partial support for Evening.
- Q7: Validation checks (V)
  - Winner placements include rank and score deltas.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Use “VTRAC top-10 + winners-lens substring/tags” as a strong convergence for Evening.
- Q10: Analyst’s extra insight
  - This is a good example of VTRAC supporting a double-ish canonical (445) while Stable is only moderate.

---

### 2.Hot Zones — PuertoRico4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2025-06-23)

## Midday winner 858 (canonical 588)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 207
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 454 (canonical 445)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 119
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 155 | vt_triad 12 | score_mean 23.858 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 469 | vt_triad 255 | score_mean 23.182 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    3 | triad 338 | vt_triad 44 | score_mean 22.452 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 168 | vt_triad 224 | score_mean 22.391 | tags funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    5 | triad 006 | vt_triad 12 | score_mean 22.3 | tags col1,guard_set1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 566 | vt_triad 12 | score_mean 21.979 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 019 | vt_triad 125 | score_mean 21.34 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 166 | vt_triad 22 | score_mean 20.775 | tags hot16,hot20,hot4,literal_draw,set1_bonus,straight_lane,superhot_set1,vertical1,vt_straight
- rank    9 | triad 149 | vt_triad 255 | score_mean 20.5 | tags hot16,hot20,set1_bonus,vertical1,vertical2,vt_only_lane,vt_straight
- rank   10 | triad 118 | vt_triad 24 | score_mean 20.436 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Hot Zones is weak for both draws (858 best rank 207; 454 best rank 119).
- Q2: 4 hit criteria mapping
  - Hot Zones is not an actionable driver on this state/day.
- Q3: Output integrity
  - Top lanes + per-lane + winner_map artifacts exist; winner_map is a top-20 snapshot.
- Q4: Dominance / noise
  - Top lanes are not aligned to 588/445.
- Q5: Where the winners show up
  - Both are deep placements; treat as non-isolating.
- Q6: Miss analysis
  - Hot Zones misses both draws as isolators.
- Q7: Validation checks (V)
  - “Not in winner_map” is expected when best_rank > 20.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Do not require Hot Zones corroboration in Puerto Rico-style days; rely on VTRAC + winners lens instead.
- Q10: Analyst’s extra insight
  - Hot Zones is not useful here; avoid over-weighting it.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Evening 454: winners-lens tags + canonical substring + VTRAC idx15 top-6.
  - Midday 858: no coherent convergence.
- Conflicts/noise:
  - Stable misses Midday; Hot Zones is weak for both draws; DR does not isolate.
- Aggregator/aux hooks to test next:
  - Allow “Evening-only actionable” days and avoid forcing Midday plays from weak evidence.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-23/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=551, 910, 383, 795, 656
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=910, 795, 681, 469, 708
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=551, 383, 656, 321, 913

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=23 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=36), P2:3 (gap=24), P3:4 (gap=33)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=987 sev=B
- 334: ds=968 sev=B
- 233: ds=960 sev=B
- 034: ds=914 sev=B
- 389: ds=858 sev=B
- 225: ds=840 sev=B
- 077: ds=838 sev=B
- 344: ds=808 sev=B
- 112: ds=788 sev=B
- 229: ds=771 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=165 sev=red
  - 00: ds=70 sev=purple
  - 22: ds=47 sev=purple
  - 11: ds=35 sev=purple
  - 44: ds=33 sev=purple
  - 77: ds=29 sev=purple
  - 99: ds=18 sev=-
  - 66: ds=4 sev=-
  - 33: ds=2 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 26: ds=81 sev=red
  - 58: ds=69 sev=red
  - 05: ds=63 sev=red
  - 14: ds=54 sev=blue
  - 04: ds=52 sev=blue
  - 48: ds=50 sev=blue
  - 45: ds=46 sev=blue
  - 29: ds=44 sev=blue
  - 47: ds=39 sev=blue
  - 17: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 33:346, 4:110, 26:109, 3:97, 29:95, 23:84, 20:75, 1:72, 35:71, 14:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 33:ds=346 fs=4 fl=1 hz=0.009554140127388535, 4:ds=110 fs=24 fl=2 hz=0.02931228861330327, 26:ds=109 fs=3 fl=2 hz=0.014925373134328358, 3:ds=97 fs=27 fl=1 hz=0.03398058252427184, 29:ds=95 fs=22 fl=1 hz=0.026589595375722544, 23:ds=84 fs=28 fl=2 hz=0.03389830508474576, 20:ds=75 fs=26 fl=2 hz=0.03056768558951965, 1:ds=72 fs=2 fl=2 hz=0.006521739130434782, 35:ds=71 fs=4 fl=2 hz=0.00853658536585366, 14:ds=69 fs=47 fl=0 hz=0.050865800865800864

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S7: ds=97 flags=red+purple
- S12: ds=91 flags=red+purple
- S20: ds=90 flags=red+purple
- S2: ds=60 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=78 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=47), P2:3 (gap=12), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=953 sev=B
- 233: ds=917 sev=B
- 112: ds=872 sev=B
- 389: ds=846 sev=B
- 111: ds=797 sev=B
- 299: ds=788 sev=B
- 344: ds=783 sev=B
- 003: ds=779 sev=B
- 077: ds=765 sev=B
- 333: ds=714 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=188 sev=red
  - 33: ds=133 sev=red
  - 88: ds=82 sev=blue
  - 00: ds=48 sev=purple
  - 22: ds=23 sev=-
  - 99: ds=21 sev=-
  - 11: ds=17 sev=-
  - 44: ds=16 sev=-
  - 77: ds=14 sev=-
  - 55: ds=6 sev=-
- non_repeating:
  - 14: ds=64 sev=red
  - 35: ds=52 sev=blue
  - 89: ds=51 sev=blue
  - 15: ds=41 sev=blue
  - 26: ds=40 sev=blue
  - 12: ds=37 sev=blue
  - 58: ds=34 sev=purple
  - 29: ds=32 sev=purple
  - 04: ds=31 sev=purple
  - 05: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:292, 32:230, 16:188, 33:181, 6:115, 19:98, 23:82, 4:66, 26:54, 21:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=292 fs=0 fl=2 hz=0.008264462809917356, 32:ds=230 fs=2 fl=1 hz=0.0067385444743935305, 16:ds=188 fs=3 fl=2 hz=0.008438818565400843, 33:ds=181 fs=6 fl=2 hz=0.011278195488721804, 6:ds=115 fs=21 fl=1 hz=0.02505694760820046, 19:ds=98 fs=14 fl=3 hz=0.01925254813137033, 23:ds=82 fs=31 fl=1 hz=0.0365296803652968, 4:ds=66 fs=22 fl=0 hz=0.024864864864864864, 26:ds=54 fs=7 fl=2 hz=0.010881392818280738, 21:ds=53 fs=48 fl=0 hz=0.051391862955032126

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=96 flags=red+purple
- S20: ds=68 flags=purple
- S26: ds=61 flags=blue+purple
- S23: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=35 last_repeat_index=2

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=43), P2:0 (gap=26), P3:0 (gap=30)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=930 sev=B
- 047: ds=917 sev=B
- 444: ds=871 sev=B
- 229: ds=850 sev=B
- 299: ds=840 sev=B
- 448: ds=829 sev=B
- 122: ds=828 sev=B
- 579: ds=810 sev=B
- 114: ds=754 sev=B
- 277: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=164 sev=red
  - 22: ds=72 sev=blue
  - 77: ds=43 sev=purple
  - 00: ds=35 sev=purple
  - 11: ds=30 sev=purple
  - 44: ds=27 sev=purple
  - 99: ds=9 sev=-
  - 66: ds=2 sev=-
  - 33: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 58: ds=61 sev=red
  - 17: ds=53 sev=blue
  - 26: ds=47 sev=blue
  - 79: ds=45 sev=blue
  - 08: ds=39 sev=blue
  - 05: ds=34 sev=purple
  - 01: ds=30 sev=purple
  - 02: ds=29 sev=purple
  - 09: ds=29 sev=purple
  - 14: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:286, 26:222, 13:187, 33:173, 14:142, 20:107, 29:93, 22:92, 17:62, 5:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=286 fs=5 fl=1 hz=0.01662049861495845, 26:ds=222 fs=3 fl=2 hz=0.008415147265077139, 13:ds=187 fs=21 fl=2 hz=0.029754204398447608, 33:ds=173 fs=14 fl=1 hz=0.019393939393939394, 14:ds=142 fs=42 fl=0 hz=0.0498812351543943, 20:ds=107 fs=22 fl=4 hz=0.030162412993039445, 29:ds=93 fs=22 fl=1 hz=0.027218934911242602, 22:ds=92 fs=33 fl=1 hz=0.0379041248606466, 17:ds=62 fs=32 fl=0 hz=0.034261241970021415, 5:ds=57 fs=18 fl=2 hz=0.021321961620469083

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=99 flags=purple
- S22: ds=80 flags=purple
- S7: ds=68 flags=purple
- S4: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '7'], 'pairs': {'remaining_count': 0}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 077 -> combined:838(B); midday:765(B)
- 112 -> combined:788(B); midday:872(B)
- 229 -> combined:771(B); evening:850(B)
- 233 -> combined:960(B); midday:917(B)
- 299 -> evening:840(B); midday:788(B)
- 344 -> combined:808(B); midday:783(B)
- 358 -> combined:987(B); evening:930(B)
- 389 -> combined:858(B); midday:846(B)
- 555 -> evening:693(B); midday:688(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:70(purple); evening:35(purple); midday:48(purple)
- 04 -> combined:52(blue); evening:26(purple); midday:31(purple)
- 05 -> combined:63(red); evening:34(purple); midday:31(purple)
- 11 -> combined:35(purple); evening:30(purple)
- 14 -> combined:54(blue); evening:27(purple); midday:64(red)
- 17 -> combined:35(purple); evening:53(blue)
- 22 -> combined:47(purple); evening:72(blue)
- 26 -> combined:81(red); evening:47(blue); midday:40(blue)
- 28 -> combined:32(purple); midday:27(purple)
- 29 -> combined:44(blue); midday:32(purple)
- 44 -> combined:33(purple); evening:27(purple)
- 45 -> combined:46(blue); midday:31(purple)
- 47 -> combined:39(blue); evening:25(purple)
- 48 -> combined:50(blue); evening:25(purple); midday:27(purple)
- 58 -> combined:69(red); evening:61(red); midday:34(purple)
- 77 -> combined:29(purple); evening:43(purple)
- 88 -> combined:165(red); evening:164(red); midday:82(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(2.4424214285714285)[R3,XVAR-Cons(CE)], 7(1.8610357142857141)[R1,Mirror-Echo], 0(1.8)[R1,Double-Pressure], 3(1.7449999999999999)[R1,Double-Pressure], 8(1.3739999999999999)[R2,Double-Pressure]
- P2: 3(3.782571428571428)[R1,XVAR-Cons(CM)], 4(2.7796)[R2,XVAR-Cons(CE)], 7(2.534957142857143)[R3,XVAR-Cons(CM)], 0(1.4762857142857142)[R1,Double-Pressure], 9(1.1108)[R2,Mirror-Echo]
- P3: 4(7.195514285714286)[R1,XVAR-Cons(CEM)], 7(3.0173428571428573)[R3,Mirror-Echo], 2(2.9623999999999997)[R2,Mirror-Echo], 0(1.4957142857142856)[R1,Double-Pressure], 6(1.1672857142857143)[R1,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-23/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-23 --state PuertoRico4 --strict` → OK.
- Q2:
  - Positional top digits:
    - Combined: 0/3/4; Midday: 3/3/6; Evening: 7/0/0.
  - These do not isolate 588/445; treat as context only.
- Q3:
  - Positional shortlist is broad; use only if it converges with an Evening candidate set.
- Q4:
  - Repeat watch current_index:
    - Combined=2; Midday=9; Evening=2 (does not match winners’ indices 13/15).
- Q5:
  - VTRAC overdue overlay:
    - Winner idx15 is modestly due in Evening (ds=23); winner idx13 is due in Evening (ds=187) but VTRAC ranking is weak for idx13.
- Q6:
  - Due doubles are extreme; not directly isolating winners.
- Q7:
  - Pairs/pairs-remaining are not decisive on this date.
- Q8:
  - Sums/pairs alerts exist but are low-discrimination.
- Q9:
  - Blackapple is low (score=1 across variants); treat as non-decisive.
- Q10:
  - Actionability:
    - Aux is context only; the actionable path is Evening 454 via winners-lens + VTRAC + (weak) Stable corroboration.

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
  - No strong isolate; avoid unless additional corroboration exists (Stable miss + Hot Zones deep).
- Candidate universe (Evening):
  - Primary: `445` box (covers 454) and/or VTRAC idx15 family coverage (8 straights).
- Evidence vectors:
  - Evening: dense winners-lens tags + canonical substring evidence + VTRAC idx15 top-6.
- Coverage mapping + pack decision:
  - Keep spend tight: box `445` (Evening); avoid Midday.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Evening: `445` box would have hit (perm set contains 454).
  - Midday: no recommended pack; evidence was weak.
- Key tags:
  - 454: very high Evening hit-family-gap (128) + hit-vt-straight (68) + canonical substring (9).
  - 858: no hit-winner tags; mostly family/gap pressure.
- Drivers:
  - Evening win is driven by winners-lens evidence + VTRAC support; Stable is secondary.
- Conflicts:
  - Midday is diffuse; Hot Zones is weak for both; DR does not isolate.
- Fix-now vs fix-later:
  - Fix-now: none.
  - Fix-later: DR Combined winner uses 551 for this state/date; investigate why Combined is not using the Midday winner (template filling can proceed regardless).
- Next run:
  - Proceed to SouthCarolina4 for 2025-06-23.
