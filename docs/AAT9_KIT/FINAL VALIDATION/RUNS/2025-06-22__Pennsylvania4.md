# Master Validation Run Report — Pennsylvania4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/Pennsylvania4/`
- Winners lens: `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2025-06-22/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2025-06-22/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2025-06-22/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2025-06-22/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2025-06-22/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2025-06-22/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac33_winner_398_20251221_222132.html`
- `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac3_winner_570_20251221_222133.html`

Winners JSON files:
- `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac33_winner_398_20251221_222132.json`
- `sharepacks/2025-06-22/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac3_winner_570_20251221_222133.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are active, and they show a very strong “8-centered” environment (with variant-specific universes).
  - Set1/Draw1 ladders (from winners JSON; same in both winner files):
    - Midday: col1 `9228** / 2298** / 8922** / 9822**`; col2 `92287** / 22987** / 87922** / 79822**`
    - Evening: col1 `008**`; col2 `038** / 083** / 803**`
    - Combined: col1 `008**`; col2 `038** / 083** / 803**`
- Q2: Column persistence is high (especially Evening/Combined `008**`), suggesting a strong “0/8/3” lane story, while Midday shows a “9/2/8” lane story.
- Q3: Winner tagging exists, but it’s largely via `hit-winner` tags rather than literal/canonical text:
  - 398 (canon 389): `hit-winner` cells=29; literal substring cells=0; canonical substring cells=0.
  - 570 (canon 057): `hit-winner` cells=13; literal substring cells=0; canonical substring cells=0.
- Q4: Variant bias and cross-variant “bounce” is plausible here:
  - Midday lane leans `9/2/8`, Evening/Combined leans `0/8/3`.
  - Midday winner 398 (3/8/9) looks like a cross-variant intersection candidate (shares 8 with both; 9 from Midday; 3 from Evening/Combined).
  - Evening winner 570 (0/5/7) is not narrated by the dominant ladders (only digit `0` overlaps).
- Q5: Permutation lane clarity is high; Midday looks like a day where a small intersection hedge could be justified, while Evening looks lower-confidence.
- Q6: Environment verdict: mixed day
  - Midday: moderate confidence (multiple tools give non-trivial corroboration).
  - Evening: low confidence (weak tool corroboration).
- Q7: Hot Zones overlap is asymmetric:
  - 398 best rank 66 (meaningful support vs other days).
  - 570 best rank 169 (weak).
  - Both have `triad_present=False` in the winner_map snapshot (expected for deep ranks).
- Q8: Cross-set carryover exists (Stable places 398 in an Evening section/chain), consistent with the “bounce” interpretation above.
- Q9: Aux cues:
  - Positional top digits: Combined `1/3/2`, Midday `1/3/2`, Evening `7/5/2` (Evening partially aligns to 570’s 7/5, but misses 0).
  - Repeat watch current_index is 8 for Combined/Evening (matches the “8 environment” feel) but not the winners’ indices (33 and 3).
- Q10: 4 hit criteria viability (pre-results lens):
  - Midday: moderate (there is enough corroboration to justify a small hedge).
  - Evening: low (treat as pass/tiny).
- Q11: Exact triple presence (winners lens):
  - 398 / canonical 389: literal substring cells=0; canonical substring cells=0; `hit-winner` cells=29.
  - 570 / canonical 057: literal substring cells=0; canonical substring cells=0; `hit-winner` cells=13.
- Q12: “Profitable environment” summary:
  - This is closer to a “positive-control” day for cross-variant structure (8-centered ladders) than a pure random miss day, at least for Midday.
- Q13: Dominance vs dilution:
  - Digit 8 dominance is real; it supports 398 (contains 8) but not 570 (no 8).
- Q14: Noise check:
  - Overall manageable noise for Midday; higher noise for Evening.
  - Fix-later note: DR Combined overlay uses a winner value (925) that does not match Pennsylvania’s results (likely a results lookup/mapping issue).

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — Pennsylvania4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2025-06-22)

## Midday winner 398 (canonical 389)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=28 | family_rows=76 | exact_boxed=28 | exact_straight=28 | vt_boxed=28
- Scores (patterns_scores.csv): rank 115, section Evening, Set Set1, Draw Draw4, Col 1, score 22.5, hot 2, vt_straight 2.0 | why straight|cov2|hp_repeat3|vstr2|mirror|hot2|hidden3v|vtrac_straight|draw_chain4
- Compound (patterns_compound.csv): rank 32, section Evening, score 42.0, col1_hits 4, hot2 4, set_chain 1, draw_chain 4 | why draw_chain4|col1x4|hot1x1|hot2x4|vstrx9
- Families (patterns_families.csv): 31 rows contain digits; best rank 220, section Evening, score 20.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=29

## Evening winner 570 (canonical 057)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=13 | family_rows=199 | exact_boxed=13 | exact_straight=13 | vt_boxed=13
- Scores (patterns_scores.csv): rank 585, section Combined, Set Set1, Draw Draw4, Col 2, score 17.0, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat3|mirror|hot2|vtrac_straight|draw_chain5
- Compound (patterns_compound.csv): rank 96, section Combined, score 31.0, col1_hits 3, hot2 2, set_chain 1, draw_chain 5 | why draw_chain5|col1x3|hot1x1|hot2x2|vstrx5
- Families (patterns_families.csv): 61 rows contain digits; best rank 17, section Evening, score 26.5, hot2 7
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=17

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 229 | section Midday | score 75.0 | col1_hits 7 | hot2 11
- rank    3 | canon 228 | section Midday | score 69.0 | col1_hits 5 | hot2 7
- rank   12 | canon 2289 | section Midday | score 53.0 | col1_hits 4 | hot2 7
- rank    7 | canon 038 | section Evening | score 58.0 | col1_hits 3 | hot2 7
- rank   32 | canon 289 | section Midday | score 42.0 | col1_hits 4 | hot2 6
- rank   20 | canon 134 | section Evening | score 46.0 | col1_hits 3 | hot2 6
- rank    4 | canon 899 | section Combined | score 60.5 | col1_hits 5 | hot2 6
- rank   10 | canon 1899 | section Combined | score 56.0 | col1_hits 5 | hot2 6
- rank    9 | canon 038 | section Combined | score 56.5 | col1_hits 0 | hot2 6
- rank    2 | canon 022 | section Midday | score 70.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1369 | family 1 | score 8.0 | hot2 0 | section Midday
- rank 1186 | family 15 | score 10.5 | hot2 0 | section Midday
- rank  220 | family 18 | score 20.0 | hot2 1 | section Midday
- rank  220 | family 21 | score 20.0 | hot2 4 | section Midday
- rank  400 | family 8 | score 18.0 | hot2 2 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - 398 (canon 389): strong Stable placement (scores rank 115; compound rank 32) even though it lands in an Evening section/chain.
  - 570 (canon 057): weaker but present (scores rank 585; compound rank 96).
- Q2: 4 hit criteria mapping
  - Both winners have exact boxed/straight=True and VT boxed support (vt_boxed=28 for 398; vt_boxed=13 for 570).
- Q3: Winners output alignment
  - Stable spotlight/scores/compound/metrics are internally consistent; no missing brain artifacts.
- Q4: Dominance / noise
  - Stable’s top compounds include strong non-winner clusters (229/228/899/038…), but 389 is still reasonably competitive (rank 32).
- Q5: Where the winners show up
  - 398 appears in Evening section (draw_chain4) which fits the cross-variant narrative (Evening/Combined ladders include `038**` / `083**` / `803**`).
  - 570 appears in Combined section (draw_chain5), but is much weaker.
- Q6: Miss analysis
  - Midday: positive-control style “tool found the winner” day (good to keep as a reference).
  - Evening: weak isolation (still far from top compounds).
- Q7: Validation checks (V)
  - Outputs present; no missing brain artifacts.
- Q8: Optimization notes
  - None now (avoid tuning from one day).
- Q9: Cross-tool synergy seed
  - Stable’s `038` candidates (top compound appears in Evening/Combined) match the winners-lens Evening/Combined ladder universe (`038/083/803`) and likely contribute to 398’s cross-variant convergence.
- Q10: Analyst’s extra insight
  - Stable is capturing Midday 398 well enough to treat this state/day as a “working example” when calibrating how much evidence is “enough” to justify a small hedge.

---

### 2.Digit Reduction — Pennsylvania4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20251222)

## Midday winner 398 (canonical 389)
- Stamp (winner_stamp.json): items_total=50 | exact_any=0 exact_final=0 | vtrac_any=17 vtrac_final=0 | drop_exact_any=22 drop_exact_final=0 | drop_vtrac_any=43 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=5 family_vtrac_final=0
- Flags (winner_flags.csv): rows=50 | exact_any=0 vtrac_any=17 | drop_exact_any=22 drop_vtrac_any=43 | family_exact_any=0 family_vtrac_any=5 | vt_boxed=50 vt_straight=0
- Hits (winner_hits.csv): rows=50 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=50 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 570 (canonical 057)
- Stamp (winner_stamp.json): items_total=26 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=26 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=26 | exact_any=0 vtrac_any=0 | drop_exact_any=3 drop_vtrac_any=26 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=2 vt_straight=0
- Hits (winner_hits.csv): rows=26 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=2 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 925 (canonical 259)
- Stamp (winner_stamp.json): items_total=568 | exact_any=12 exact_final=0 | vtrac_any=340 vtrac_final=0 | drop_exact_any=60 drop_exact_final=0 | drop_vtrac_any=507 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=158 family_vtrac_final=0
- Flags (winner_flags.csv): rows=568 | exact_any=12 vtrac_any=340 | drop_exact_any=60 drop_vtrac_any=507 | family_exact_any=0 family_vtrac_any=158 | vt_boxed=54 vt_straight=0
- Hits (winner_hits.csv): rows=568 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=54 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 599 | score_v2 13.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 13.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 599 | score_v2 13.477143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 599 | score_v2 13.427143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 599 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 599 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 12.727143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 13.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 599 | score_v2 12.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 922 | score_v2 12.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 559 | score_v2 11.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 922 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 922 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 224 | score_v2 11.537143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 599 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Evening | best_pattern 599 | score_v2 11.437143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 922 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR does not isolate 398 or 570 as top candidates (`winner_triads_as_candidates=False`).
  - Midday 398: some VTRAC/drop coverage exists (vtrac_any=17; drop_vtrac_any=43) but no finals.
  - Evening 570: no vtrac_any; mostly drop_vtrac_any; still no finals.
  - Combined overlay is suspect: it uses winner=925 (not Pennsylvania’s results) and date=None.
- Q2: Stamp interpretation
  - Midday 398: vt_boxed=50 suggests broad boxed coverage, not narrow isolation.
  - Evening 570: vt_boxed=2 and some drop_exact_any=3, but still not isolating.
  - Combined: treat as non-gradeable until the winner mapping is corrected.
- Q3: 4 hit criteria mapping
  - DR is operating as “coverage flags”, not a tight caller here (no exact finals; vtrac finals all 0).
- Q4: Dominance / noise
  - Top per_item patterns are dominated by 599/922 families rather than the winners.
- Q5: Where the winners show up
  - Only as broad any-flags; not as top candidates.
- Q6: Miss analysis
  - DR is effectively a miss day for both winners (for actionable isolation).
- Q7: Validation checks (V)
  - Flag as fix-later: Combined winner stamp (925) mismatches the results for Pennsylvania; likely a results lookup/state mapping issue in DR overlay generation.
- Q8: Optimization notes
  - None now; first fix is correctness of the Combined winner mapping for DR.
- Q9: Cross-tool synergy seed
  - DR top patterns (`599`/`922`) align with general lane dominance but don’t explain 398/570.
- Q10: Analyst’s extra insight
  - For this day, DR should be treated as “background context” rather than a decider.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20251221_222527)

## Top indices (from enhanced JSON)
- index 27 | score 84.19604499999996 | features: presence=51.69854499999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 66.77572499999998 | features: presence=37.58822499999999, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 28 | score 30.005650000000003 | features: presence=19.87815, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 30 | score 27.721750000000004 | features: presence=19.018000000000004, first_hit=0.4, column_span=0.29375, persistence=0.4
- index 32 | score 27.11505500000001 | features: presence=18.667555000000007, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 31 | score 11.177958333333335 | features: presence=4.979000000000001, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 11 | score 9.887749999999999 | features: presence=2.4639999999999995, cross_section=0.5, set_echo=0.6, first_hit=0.08000000000000002
- index 20 | score 9.396118333333332 | features: presence=3.30716, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336
- index 23 | score 9.332618333333333 | features: presence=5.253659999999999, set_echo=0.6, first_hit=0.13333333333333336, column_span=0.06562499999999999
- index 21 | score 6.976768333333333 | features: presence=2.48781, cross_section=0.5, set_echo=0.6, first_hit=0.13333333333333336

## Top straights (from enhanced JSON)
287, 832, 238, 872, 732, 283, 837, 873, 982, 298

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 398 | index 33 | file Pennsylvania4_vtrac33_winner_398_20251221_222132.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 570 | index 3 | file Pennsylvania4_vtrac3_winner_570_20251221_222133.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 398 | index 33 rank 14/35 | score 3.8207500000000003 | winner_in_index_straights=False | top_index_straights: 893 (0.269), 983 (0.269)
- winner 570 | index 3 rank 19/35 | score 1.962875 | winner_in_index_straights=False | top_index_straights: (none)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - 398: idx33 rank 14/35 (score ~3.82) → weak/moderate.
  - 570: idx3 rank 19/35 (score ~1.96) → weak.
- Q2: 4 hit criteria mapping
  - `winner_in_index_straights=False` for both winners (top straights list does not contain them).
- Q3: Winners output alignment
  - VTRAC outputs are consistent with winners lens indices (33 and 3); they’re simply not favored in the ranking.
- Q4: Dominance / noise
  - Top indices are 27/29/28/30/32…, not 33/3.
- Q5: Where the winners show up
  - Both are mid/low tier; neither is a strong VTRAC call.
- Q6: Miss analysis
  - Treat as VTRAC analyzer miss day (Stable/HotZones carried the Midday win instead).
- Q7: Validation checks (V)
  - Outputs present; no missing artifacts.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - The “8 environment” seen in winners lens and repeat watch (current_index=8) did not translate into VTRAC index ranking strength; worth tracking across more days.
- Q10: Analyst’s extra insight
  - Keep VTRAC analyzer as a secondary corroborator here; it’s not the primary source of the win on this day.

---

### 2.Hot Zones — Pennsylvania4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2025-06-22)

## Midday winner 398 (canonical 389)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 66
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 570 (canonical 057)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 169
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 227 | vt_triad 33 | score_mean 22.85 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    1 | triad 277 | vt_triad 33 | score_mean 22.85 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    4 | triad 278 | vt_triad 334 | score_mean 21.714 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    5 | triad 237 | vt_triad 334 | score_mean 21.659 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    6 | triad 667 | vt_triad 23 | score_mean 21.157 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    7 | triad 267 | vt_triad 233 | score_mean 20.658 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    7 | triad 127 | vt_triad 233 | score_mean 20.658 | tags funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    9 | triad 226 | vt_triad 23 | score_mean 20.552 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 036 | vt_triad 124 | score_mean 19.839 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - 398: present with best rank 66 (meaningful support).
  - 570: present with best rank 169 (weak).
  - Winner map triad snapshot is present but `triad_present=False` for both (top-20 snapshot limitation).
- Q2: 4 hit criteria mapping
  - Per-lane indicates has_straight=True and has_vt_straight=True for winners, but only 398 is ranked well enough to matter.
- Q3: Winners output alignment
  - “winner_not_in_winner_map” is expected when the winner is outside the top-20 (+guard) snapshot; do not treat as corruption.
- Q4: Dominance / noise
  - Top lanes emphasize `227/277/000/278/237/...` which do not narrate 389/057.
- Q5: Where the winners show up
  - 398: modestly actionable (rank 66).
  - 570: weak corroboration only.
- Q6: Miss analysis
  - Midday: Hot Zones adds corroboration to Stable’s win.
  - Evening: miss/weak day for Hot Zones.
- Q7: Validation checks (V)
  - Outputs present; no missing artifacts.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Treat Hot Zones as a “support vote”: when it ranks the winner in the low double-digits (like 66), it’s meaningful corroboration for Stable-driven candidates.
- Q10: Analyst’s extra insight
  - This state/day is a good example where Hot Zones improves confidence for Midday but not for Evening, reinforcing the need for draw-specific posture.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Strong “8 environment” in winners lens (Evening/Combined `008**` and `038/083/803` ladders) + repeat watch current_index=8 (Combined/Evening).
  - Stable + Hot Zones both provide meaningful support for Midday 398 (Stable compound rank 32; Hot Zones best rank 66).
- Conflicts/noise:
  - Evening 570 is weakly corroborated by tools; it is mostly off-board.
  - DR Combined overlay appears to use the wrong winner value (925) for this state/day.
- Aggregator/aux hooks to test next:
  - Track “cross-variant intersection” situations (Midday 9/2/8 lane + Evening 0/8/3 lane → 3/8/9 outcomes) as a hypothesis class.
  - Fix-later: confirm/fix DR Combined results lookup so Combined overlays don’t pull the wrong state’s winner.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=360, 667, 226, 354, 846
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=667, 354, 041, 954, 578
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=360, 226, 846, 567, 917

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=121 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=25), P2:3 (gap=41), P3:2 (gap=27)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=874 sev=B
- 012: ds=858 sev=B
- 455: ds=802 sev=B
- 467: ds=732 sev=B
- 059: ds=713 sev=B
- 244: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=51 sev=purple
  - 77: ds=49 sev=purple
  - 00: ds=44 sev=purple
  - 44: ds=43 sev=purple
  - 11: ds=21 sev=-
  - 88: ds=18 sev=-
  - 33: ds=13 sev=-
  - 99: ds=12 sev=-
  - 22: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 15: ds=51 sev=blue
  - 38: ds=50 sev=blue
  - 39: ds=41 sev=blue
  - 23: ds=35 sev=purple
  - 37: ds=32 sev=purple
  - 07: ds=31 sev=purple
  - 18: ds=29 sev=purple
  - 47: ds=27 sev=purple
  - 27: ds=24 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:255, 26:186, 1:154, 32:149, 4:138, 35:112, 6:84, 33:68, 5:65, 27:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=255 fs=3 fl=2 hz=0.008241758241758242, 26:ds=186 fs=0 fl=1 hz=0.005649717514124294, 1:ds=154 fs=5 fl=3 hz=0.010126582278481013, 32:ds=149 fs=2 fl=1 hz=0.005738880918220947, 4:ds=138 fs=20 fl=1 hz=0.02530120481927711, 35:ds=112 fs=2 fl=0 hz=0.005917159763313609, 6:ds=84 fs=20 fl=0 hz=0.021953896816684963, 33:ds=68 fs=20 fl=1 hz=0.02260495156081808, 5:ds=65 fs=13 fl=2 hz=0.01714898177920686, 27:ds=63 fs=18 fl=3 hz=0.023127753303964757

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=69 flags=purple
- S7: ds=63 flags=purple
- S22: ds=48 flags=purple
- S0: ds=47 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=66 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=12), P2:3 (gap=20), P3:2 (gap=13)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=998 sev=B
- 118: ds=834 sev=B
- 559: ds=783 sev=B
- 018: ds=771 sev=B
- 288: ds=770 sev=B
- 255: ds=741 sev=B
- 668: ds=723 sev=B
- 199: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=25 sev=purple
  - 77: ds=24 sev=-
  - 00: ds=23 sev=-
  - 22: ds=22 sev=-
  - 44: ds=21 sev=-
  - 88: ds=14 sev=-
  - 11: ds=10 sev=-
  - 99: ds=9 sev=-
  - 33: ds=6 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 48: ds=67 sev=red
  - 25: ds=66 sev=red
  - 68: ds=50 sev=blue
  - 29: ds=49 sev=blue
  - 69: ds=46 sev=blue
  - 28: ds=45 sev=blue
  - 19: ds=44 sev=blue
  - 17: ds=39 sev=blue
  - 03: ds=38 sev=blue
  - 37: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:597, 26:181, 4:174, 1:166, 6:161, 29:133, 16:127, 25:101, 32:74, 12:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=597 fs=6 fl=1 hz=0.01881720430107527, 26:ds=181 fs=1 fl=0 hz=0.0028328611898017, 4:ds=174 fs=18 fl=2 hz=0.026075619295958277, 1:ds=166 fs=2 fl=3 hz=0.00904977375565611, 6:ds=161 fs=16 fl=1 hz=0.0228494623655914, 29:ds=133 fs=23 fl=0 hz=0.030666666666666665, 16:ds=127 fs=2 fl=5 hz=0.008728179551122194, 25:ds=101 fs=20 fl=2 hz=0.024608501118568233, 32:ds=74 fs=6 fl=1 hz=0.008781558726673985, 12:ds=65 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=88 flags=purple
- S26: ds=80 flags=blue+purple
- S1: ds=79 flags=blue+purple
- S23: ds=75 flags=purple
- S22: ds=62 flags=purple
- S14: ds=36 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 024: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 267: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 069: score=2 tags=RS
  - 078: score=2 tags=RS
  - 159: score=2 tags=RS
  - 168: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=38 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=29), P2:5 (gap=40), P3:2 (gap=43)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=40), P3:2 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=909 sev=B
- 788: ds=871 sev=B
- 557: ds=850 sev=B
- 779: ds=844 sev=B
- 278: ds=790 sev=B
- 444: ds=779 sev=B
- 899: ds=776 sev=B
- 778: ds=759 sev=B
- 009: ds=737 sev=B
- 077: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=113 sev=red
  - 55: ds=65 sev=purple
  - 33: ds=43 sev=purple
  - 66: ds=31 sev=purple
  - 44: ds=29 sev=purple
  - 00: ds=22 sev=-
  - 11: ds=15 sev=-
  - 88: ds=9 sev=-
  - 99: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 59: ds=65 sev=red
  - 07: ds=57 sev=red
  - 49: ds=56 sev=red
  - 78: ds=49 sev=blue
  - 23: ds=37 sev=blue
  - 39: ds=34 sev=purple
  - 15: ds=33 sev=purple
  - 89: ds=32 sev=purple
  - 47: ds=29 sev=purple
  - 12: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:423, 3:262, 16:210, 28:150, 26:93, 15:81, 1:77, 17:72, 4:69, 5:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=423 fs=0 fl=1 hz=0.004405286343612335, 3:ds=262 fs=12 fl=2 hz=0.020710059171597635, 16:ds=210 fs=4 fl=4 hz=0.011142061281337047, 28:ds=150 fs=15 fl=3 hz=0.02120141342756184, 26:ds=93 fs=2 fl=0 hz=0.005242463958060288, 15:ds=81 fs=35 fl=0 hz=0.042682926829268296, 1:ds=77 fs=8 fl=3 hz=0.013480392156862744, 17:ds=72 fs=24 fl=1 hz=0.02824858757062147, 4:ds=69 fs=28 fl=1 hz=0.03125, 5:ds=65 fs=15 fl=4 hz=0.020496224379719524

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=59 flags=purple
- S7: ds=53 flags=purple
- S8: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:713(B); evening:716(B)
- 255 -> evening:695(B); midday:741(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:31(purple); evening:57(red)
- 15 -> combined:51(blue); evening:33(purple); midday:25(purple)
- 23 -> combined:35(purple); evening:37(blue)
- 37 -> combined:32(purple); midday:30(purple)
- 38 -> combined:50(blue); evening:25(purple); midday:29(purple)
- 39 -> combined:41(blue); evening:34(purple)
- 44 -> combined:43(purple); evening:29(purple)
- 47 -> combined:27(purple); evening:29(purple)
- 55 -> combined:51(purple); evening:65(purple); midday:25(purple)
- 77 -> combined:49(purple); evening:113(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.157500000000001)[R1,XVAR-Cons(CEM)], 7(3.923857142857143)[R2,XVAR-Cons(CE)], 8(0.9299)[R2,Double-Pressure], 0(0.24779285714285712)[R3,Swap], 4(0.15557142857142858)[R3]
- P2: 3(8.62567857142857)[R1,Mirror-Echo], 8(3.7307785714285715)[R2,Mirror-Echo], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0553)[R2,Double-Pressure], 0(0.30153571428571424)[R3,Swap]
- P3: 2(8.181714285714285)[R1,XVAR-Cons(CEM)], 9(2.3849214285714284)[R2,XVAR-Cons(CM)], 3(1.8974142857142857)[R3,XVAR-Cons(CE)], 4(1.2761)[R2,Double-Pressure], 0(0.8998999999999999)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` (n=1000)
  - Workbook provenance: `data/history/Pick3StatsC4_2025-06-21.xlsm` (aux_state_label=Pennsylvania).
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state Pennsylvania4 --strict` → OK.
- Q2:
  - Positional pressure (by variant):
    - Combined top digits: `1/3/2`
    - Midday top digits: `1/3/2`
    - Evening top digits: `7/5/2` (partial alignment to winner 570’s 7/5)
- Q3:
  - Positional shortlist is dominated by `132/732/182/...`; neither winner appears as a top positional candidate.
- Q4:
  - Repeat watch suggests an “8 environment” but not the winners’ indices:
    - Combined current_index=8; Midday current_index=17; Evening current_index=8.
- Q5:
  - VTRAC overlay does not obviously support the winners’ indices (33 and 3) as top overdue indices.
- Q6:
  - Doubles/pairs pressure is moderate-to-high; it does not directly narrow to the winners.
- Q7:
  - Sums are broadly flagged (mostly purple / red+purple) → low discrimination.
- Q8:
  - Blackapple is low-signal (score=0 in Combined; no candidates) → treat as neutral.
- Q9:
  - Cross-variant alerts show multi-variant pair/double pressure (e.g., 059, 255), reinforcing “busy environment” posture rather than direct calls.
- Q10:
  - Use Aux as corroboration: repeat watch + ladder dominance supports the “8 environment” narrative; Stable/HotZones carry the Midday win (398), while Evening remains weak.

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
  - Smallest coherent “capture” pack: `389` boxed set (covers winner 398) — supported by Stable (compound rank 32) + Hot Zones (rank 66).
  - Optional structural hedge: include the winners-lens Evening/Combined lane `038` boxed (since 038/083/803 ladders are dominant), but keep spend tight.
- Candidate universe (Evening):
  - Default posture: pass/tiny (weak corroboration).
  - If forced: `057` boxed set is the smallest post-hoc capture (covers 570), but treat as low confidence.
- Evidence vectors:
  - Pro Midday 398: Stable strong ranks + Hot Zones decent rank + heavy winners-lens `hit-winner` tagging.
  - Contra Evening 570: weak Stable/HotZones ranks; mostly off-board.
- Coverage mapping + pack decision:
  - Midday: box-focused (6 perms of 389) is the cleanest small-spend posture.
  - Evening: pass/tiny only.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - A small Midday `389` box would have hit (winner 398).
  - Evening: there was no strong pre-results isolation; a tiny `057` box would have hit post-hoc but is low confidence.
- Key tags:
  - “8 environment” dominance in winners lens (008/038 ladders) + repeat watch current_index=8 (Combined/Evening).
  - Stable+HotZones corroboration for Midday winner 398.
- Drivers:
  - The Midday win is driven primarily by Stable (and supported by Hot Zones), not by DR/VTRAC analyzer.
- Conflicts:
  - Evening winner lacks corroboration; DR is mostly noise here.
  - DR Combined overlay winner mismatch (925) is confusing and should be treated as an artifact issue, not an analytical signal.
- Fix-now vs fix-later:
  - Fix-now: none (alignment guard passes).
  - Fix-later: DR Combined winner mapping (shows 925, date=None) likely pulling the wrong state’s result.
- Next run:
  - Continue D=2025‑06‑22 reports; Pennsylvania4 is a good “Midday positive-control / Evening weak” example.
