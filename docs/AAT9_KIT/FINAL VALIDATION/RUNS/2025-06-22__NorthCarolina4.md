# Master Validation Run Report — NorthCarolina4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/NorthCarolina4/`
- Winners lens: `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2025-06-22/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2025-06-22/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2025-06-22/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2025-06-22/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2025-06-22/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-06-22/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac7_winner_765_20251221_222124.html`
- `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac8_winner_153_20251221_222126.html`

Winners JSON files:
- `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac7_winner_765_20251221_222124.json`
- `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac8_winner_153_20251221_222126.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are very “active”, but they only clearly anchor the Evening winner when you use the Combined lens.
  - Set1/Draw1 ladders (from winners JSON):
    - Midday: col1 `036** / 063**`; col2 `2436** / 2634** / 6324** / 3624**` (0/3/6 and 2/3/4/6 universe)
    - Evening: col1/col2 `5541** / 1554** / 1455**` (1/4/5 universe)
    - Combined: col1 `41386** / 68341** / 68134** / 18364**`; col2 `413386** / 683341** / 681334** / 183364**` (1/3/4/6/8 universe)
- Q2: Column persistence is strong (dense `**` ladders + lots of survivors), but the Midday winner is not supported by printed lanes; the Evening winner is supported primarily via Combined.
- Q3: “Last survivors” density is high, and the winners are asymmetric:
  - 765: no direct `hit-winner` tagging anywhere (only broad family-gap pressure).
  - 153: strong `hit-winner` tagging appears in the Combined tables (even though it’s not printed in the Evening Set1 ladders).
- Q4: Variant bias:
  - Midday winner 765 (canon 567): off-board in Midday/Evening/Combined lane strings.
  - Evening winner 153 (canon 135): appears strongly in **Combined** (literal `153`), not in the Evening ladder strings.
- Q5: Permutation lane clarity:
  - 765: no printed lane / substring evidence.
  - 153: clear literal presence in Combined; canonical `135` is not printed as a substring.
- Q6: Environment verdict: **split**
  - Evening looks moderately playable due to Stable exact + Combined winners-lens on-board evidence.
  - Midday is weaker in Stable/DR, but Hot Zones strongly supports it (see Part 2 Hot Zones).
- Q7: Hot Zones overlap is inverted vs the winners:
  - Midday 765: strong rank (best rank 16), but winner_map triad_present=False.
  - Evening 153: very weak rank (best rank 173), winner_map triad_present=False.
- Q8: Cross-set carryover: strongest for Evening via Combined lens + Stable Combined scores/compound; Midday has little cross-tool carry.
- Q9: Aux cues (quick lens):
  - Combined positional top digits: `1/4/4` and shortlist dominated by `144/146/143/134/...` lanes (adjacent to the Evening canonical family but not a direct call).
  - VTRAC overdue indices do not include 7 or 8 (weak Aux support for winner indices).
- Q10: 4 hit criteria viability (pre-results lens):
  - Midday: only Hot Zones/VTRAC-family style support; Stable does not isolate 567.
  - Evening: Stable exact boxed/straight=True plus VTRAC idx8 moderate rank → workable as a small box.
- Q11: Exact triple presence (winners lens):
  - 765 / canonical 567: literal substring cells=0; canonical substring cells=0; `hit-winner` cells=0.
  - 153 / canonical 135: strong literal substring + `hit-winner` tagging in Combined (hit-winner cells=11); canonical substring cells=0.
- Q12: Profitable environment summary:
  - This is a strong example of “Combined lens can carry the winner even when the draw-specific (Evening) ladder doesn’t print it.”
- Q13: Dominance vs dilution:
  - The environment is dominated by 1/3/4/6/8 and 1/4/5 ladders; that supports the Evening digit universe better than the Midday 5/6/7 universe.
- Q14: Noise check:
  - Moderate-high: strong lane activity and family-gap pressure, but only the Evening winner gets a clear Combined on-board tag.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — NorthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2025-06-22)

## Midday winner 765 (canonical 567)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=160 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 42 rows contain digits; best rank 212, section Midday, score 22.0, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=64
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 153 (canonical 135)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=11 | family_rows=589 | exact_boxed=11 | exact_straight=11 | vt_boxed=11
- Scores (patterns_scores.csv): rank 538, section Combined, Set Set1, Draw Draw3, Col 1, score 20.0, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat4|hot2|vtrac_straight|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 65, section Combined, score 39.5, col1_hits 2, hot2 4, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x2|hot1x1|hot2x4|vstrx6
- Families (patterns_families.csv): 63 rows contain digits; best rank 118, section Midday, score 24.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=200

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 134 | section Combined | score 73.5 | col1_hits 7 | hot2 11
- rank    1 | canon 346 | section Combined | score 86.0 | col1_hits 9 | hot2 11
- rank    2 | canon 455 | section Evening | score 83.0 | col1_hits 7 | hot2 11
- rank   22 | canon 1455 | section Evening | score 52.5 | col1_hits 4 | hot2 9
- rank   13 | canon 556 | section Evening | score 63.5 | col1_hits 4 | hot2 9
- rank   21 | canon 145 | section Evening | score 55.0 | col1_hits 5 | hot2 9
- rank    5 | canon 155 | section Evening | score 69.0 | col1_hits 5 | hot2 9
- rank   19 | canon 3688 | section Combined | score 55.5 | col1_hits 6 | hot2 8
- rank   14 | canon 138 | section Combined | score 61.5 | col1_hits 7 | hot2 8
- rank   11 | canon 188 | section Combined | score 64.0 | col1_hits 6 | hot2 8

## Top families (patterns_families.csv)
- rank 1432 | family 4 | score 3.0 | hot2 0 | section Midday
- rank 1001 | family 12 | score 12.0 | hot2 0 | section Midday
- rank  603 | family 30 | score 16.0 | hot2 0 | section Midday
- rank  695 | family 15 | score 15.0 | hot2 0 | section Midday
- rank  695 | family 34 | score 15.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday 765 (canon 567): not present in scores/compound; only family-level presence → Stable miss as a caller.
  - Evening 153 (canon 135): exact boxed/straight=True with mid-tier ranks (scores rank 538; compound rank 65) → moderate support.
- Q2: 4 hit criteria mapping
  - Midday: no exact boxed/straight; treat as a miss.
  - Evening: exact boxed/straight + VT-straight features present (vt_straight=2.0).
- Q3: Winners output alignment
  - Stable artifacts are internally consistent; Evening is a real exact hit, Midday is a real miss (not missing-data noise).
- Q4: Dominance / noise
  - Stable’s top compounds are dominated by other canonicals (346, 455, 134, 155, ...) which are close to the Evening family universe.
- Q5: Where the winners show up
  - 135: present in scores/compound and spotlight (actionable).
  - 567: family-only presence (not actionable).
- Q6: Miss analysis
  - Midday: hard miss.
  - Evening: moderate hit (not top-tier, but real).
- Q7: Validation checks (V)
  - Outputs present; no missing artifacts.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Evening winner is supported by: Stable exact + VTRAC idx8 moderate rank + Combined winners-lens `hit-winner` tags.
- Q10: Analyst’s extra insight
  - The Evening winner is mainly a Combined-leaning Stable hit (scores/compound in Combined), which matches the “Combined lens carries the winner” story in Part A.

---

### 2.Digit Reduction — NorthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20251222)

## Midday winner 765 (canonical 567)
- Stamp (winner_stamp.json): items_total=36 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=36 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=11 family_vtrac_final=0
- Flags (winner_flags.csv): rows=36 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=36 | family_exact_any=0 family_vtrac_any=11 | vt_boxed=12 vt_straight=0
- Hits (winner_hits.csv): rows=36 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=12 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 153 (canonical 135)
- Stamp (winner_stamp.json): items_total=51 | exact_any=3 exact_final=0 | vtrac_any=47 vtrac_final=0 | drop_exact_any=3 drop_exact_final=0 | drop_vtrac_any=14 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=3 family_vtrac_final=0
- Flags (winner_flags.csv): rows=51 | exact_any=3 vtrac_any=47 | drop_exact_any=3 drop_vtrac_any=14 | family_exact_any=0 family_vtrac_any=3 | vt_boxed=15 vt_straight=0
- Hits (winner_hits.csv): rows=51 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=15 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 765 (canonical 567)
- Stamp (winner_stamp.json): items_total=91 | exact_any=0 exact_final=0 | vtrac_any=37 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=91 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=11 family_vtrac_final=0
- Flags (winner_flags.csv): rows=91 | exact_any=0 vtrac_any=37 | drop_exact_any=0 drop_vtrac_any=91 | family_exact_any=0 family_vtrac_any=11 | vt_boxed=43 vt_straight=0
- Hits (winner_hits.csv): rows=91 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=43 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 554 | score_v2 13.727143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 554 | score_v2 13.527143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw6 col 2 | pattern 554 | score_v2 13.477143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw4 col 2 | pattern 554 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 554 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw3 col 2 | pattern 554 | score_v2 13.227143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 554 | score_v2 12.977143 | match_types 
- area_rank 2 | variant Evening | section Evening | set Set1 draw Draw6 col 1 | pattern 554 | score_v2 12.377143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 10.987143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 7 | pattern 559 | score_v2 10.287143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Evening | best_pattern 554 | score_v2 13.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 10.987143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 559 | score_v2 10.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 524 | score_v2 10.047143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 441 | score_v2 9.965714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 9.49381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 559 | score_v2 9.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 524 | score_v2 9.247143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 441 | score_v2 9.165714 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 554 | score_v2 9.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR does not isolate either winner as a top candidate (winner_present=False for both).
- Q2: Stamp interpretation
  - 765: broad drop-vtrac membership (drop_vtrac_any=36) and some vtrac_any membership, but no candidate isolation.
  - 153: some exact_any=3 and vtrac_any=47 membership, but still no candidate isolation or finals.
- Q3: What DR wanted (top patterns)
  - DR’s dominant patterns are `554` and `559` (strong 5/4 lane pressure), matching the Evening ladder universe (`5541/1554/1455`).
- Q4: Winner-lane notes
  - DR does not narrow to 567 or 135 as candidates; it stays on the 554/559 lane family.
- Q5: Signal strength vs noise
  - Useful as a context meter (“5/4 pressure”), not a caller here.
- Q6: Miss analysis
  - Treat as an honest miss for DR as a direct isolator on this day.
- Q7: Validation checks (V)
  - Scores present; winners artifacts exist for Midday/Evening/Combined; no integrity issues observed.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - DR’s 554/559 dominance aligns with Stable’s strong 455 family and the Evening winners-lens ladder universe (even if it didn’t isolate the exact winner).
- Q10: Analyst’s extra insight
  - DR is reinforcing “lane shape” rather than providing a direct call; keep this in mind for superbrain aggregation.

---

### 2.VTRAC Analyzer — NorthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20251221_222524)

## Top indices (from enhanced JSON)
- index 23 | score 83.18642749999997 | features: presence=63.12892749999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 63.46114249999998 | features: presence=43.98364249999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 19 | score 53.367562499999984 | features: presence=34.35006249999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 46.279495 | features: presence=31.621995000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 39.574575 | features: presence=24.307075, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 16 | score 28.364300000000004 | features: presence=17.896800000000002, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 28.2594525 | features: presence=19.841952499999998, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 23.90867 | features: presence=16.01117, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 8 | score 23.75591666666667 | features: presence=15.991750000000003, set_echo=0.6, first_hit=0.4, column_span=0.25416666666666665
- index 17 | score 20.432130000000004 | features: presence=9.984630000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
624, 386, 683, 183, 681, 413, 641, 813, 136, 138

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 765 | index 7 | file NorthCarolina4_vtrac7_winner_765_20251221_222124.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 153 | index 8 | file NorthCarolina4_vtrac8_winner_153_20251221_222126.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 765 | index 7 rank 15/35 | score 15.0256 | winner_in_index_straights=False | top_index_straights: 206 (7.74), 062 (4.372), 602 (4.372)
- winner 153 | index 8 rank 9/35 | score 23.75591666666667 | winner_in_index_straights=False | top_index_straights: 036 (10.524), 063 (8.081), 603 (5.155)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Winner idx7 (765): rank 15/35 (moderate).
  - Winner idx8 (153): rank 9/35 (moderate).
- Q2: What VTRAC wanted (top straights)
  - Top straights are other families (`624/386/683/183/681/.../136/138`), not the winners.
- Q3: Winner index isolation
  - VTRAC does not decisively isolate idx7 or idx8 (both are “in the mix”, not dominant).
- Q4: Consensus / cross-section
  - consensus_col1/2 flags are False; ranking is driven by presence features.
- Q5: Miss analysis
  - Treat VTRAC as moderate corroboration (especially for Evening idx8), not decisive.
- Q6: Validation checks (V)
  - Artifacts exist; winners lens present.
- Q7: Cross-tool synergy seed
  - Evening outcome benefits from multi-layer moderate corroboration (Stable exact + VTRAC rank 9 + Combined winners-lens tagging).
- Q8: Optimization notes
  - None now.
- Q9: Aux hook
  - Aux overdue list does not elevate idx7 or idx8; treat Aux VTRAC overlay as non-supportive here.
- Q10: Analyst’s extra insight
  - This is a “mid confidence” VTRAC day: two winner indices are not top, but not buried either.

---

### 2.Hot Zones — NorthCarolina4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2025-06-22)

## Midday winner 765 (canonical 567)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 16
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 153 (canonical 135)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 173
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 247 | vt_triad 335 | score_mean 23.603 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 379 | vt_triad 345 | score_mean 23.236 | tags col1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 237 | vt_triad 334 | score_mean 21.963 | tags hot16,hot20,set1_bonus,straight_lane,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 077 | vt_triad 13 | score_mean 21.77 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 278 | vt_triad 334 | score_mean 21.738 | tags hot16,hot20,set1_bonus,vertical2,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 257 | vt_triad 133 | score_mean 21.406 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 126 | vt_triad 223 | score_mean 21.139 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 022 | vt_triad 13 | score_mean 21.005 | tags hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 029 | vt_triad 135 | score_mean 20.75 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 169 | vt_triad 225 | score_mean 20.306 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Midday 765: strong Hot Zones rank (best rank 16), but vt-only lane (has_straight=False).
  - Evening 153: very weak Hot Zones rank (best rank 173) even though has_straight=True.
- Q2: 4 hit criteria mapping
  - Midday: vt-straight membership is present (has_vt_straight=True); treat as “family/VT” support only.
  - Evening: has_straight=True and has_vt_straight=True, but rank is too weak to treat as decisive.
- Q3: Winner map interpretation
  - triad_present=False for both winners is expected given the winner_map is a top-slice; treat as weakness, not corruption.
- Q4: What Hot Zones wanted (top lanes)
  - Top lanes are dominated by other triads (247/379/237/077/...), indicating a very different dominant lane universe than the Evening winner.
- Q5: Miss analysis
  - Hot Zones strongly “liked” the Midday winner (rank 16) but did not like the Evening winner (rank 173).
- Q6: Validation checks (V)
  - Outputs exist; winner map files present.
- Q7: Cross-tool synergy seed
  - Midday: Hot Zones (rank 16) + VTRAC idx7 rank 15 are the best corroborators, even though Stable missed.
- Q8: Optimization notes
  - None now.
- Q9: Aux hook
  - Aux positional shortlist (144/146/143/134...) aligns more with Combined dominance than with either winner; treat as context.
- Q10: Analyst’s extra insight
  - This is a useful example of tool disagreement: Hot Zones calls Midday well, while Stable calls Evening better — valuable for later aggregator weighting.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Strong 1/3/4/6 lane dominance in Combined (winners-lens Combined ladders + Aux positional top digits/shortlist).
  - Evening winner (153) is supported by Stable exact + VTRAC idx8 mid-rank + Combined winners-lens hit-winner tags.
- Conflicts/noise:
  - Midday winner (765) is well-ranked by Hot Zones but is a Stable miss.
  - Evening winner (153) is a Hot Zones weak rank despite Stable exact + Combined-lens visibility.
- Aggregator/aux hooks to test next:
  - Treat “Combined winners-lens on-board” as an explicit confidence booster (especially when draw-specific ladder does not show the winner).
  - Track “Hot Zones strong, Stable miss” cases (like Midday here) as a candidate family-only hedge pattern.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=397, 427, 261, 707, 902
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=427, 707, 579, 257, 718
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=397, 261, 902, 799, 800

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=5 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=31), P2:4 (gap=15), P3:4 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=829 sev=B
- 228: ds=822 sev=B
- 244: ds=796 sev=B
- 004: ds=770 sev=B
- 001: ds=734 sev=B
- 677: ds=695 sev=B
- 377: ds=693 sev=B
- 044: ds=691 sev=B
- 226: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=101 sev=blue
  - 44: ds=55 sev=purple
  - 66: ds=48 sev=purple
  - 11: ds=38 sev=purple
  - 33: ds=36 sev=purple
  - 22: ds=27 sev=purple
  - 55: ds=26 sev=purple
  - 00: ds=8 sev=-
  - 99: ds=6 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 89: ds=130 sev=red
  - 46: ds=98 sev=red
  - 15: ds=75 sev=red
  - 13: ds=41 sev=blue
  - 36: ds=36 sev=purple
  - 49: ds=33 sev=purple
  - 14: ds=31 sev=purple
  - 23: ds=30 sev=purple
  - 67: ds=28 sev=purple
  - 06: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:375, 16:243, 35:199, 29:151, 15:105, 26:92, 2:76, 6:75, 27:59, 25:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=375 fs=0 fl=2 hz=0.0049504950495049506, 16:ds=243 fs=0 fl=1 hz=0.0036900369003690036, 35:ds=199 fs=0 fl=2 hz=0.005154639175257732, 29:ds=151 fs=19 fl=1 hz=0.02442002442002442, 15:ds=105 fs=21 fl=0 hz=0.025059665871121718, 26:ds=92 fs=3 fl=1 hz=0.007109004739336493, 2:ds=76 fs=22 fl=0 hz=0.024017467248908297, 6:ds=75 fs=23 fl=3 hz=0.029213483146067414, 27:ds=59 fs=12 fl=1 hz=0.016587677725118485, 25:ds=55 fs=17 fl=4 hz=0.022364217252396165

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=84 flags=purple
- S2: ds=82 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=2 last_repeat_gap=15 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=19), P2:3 (gap=20), P3:3 (gap=63)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:3 (ds=63)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 344: ds=829 sev=B
- 188: ds=822 sev=B
- 558: ds=779 sev=B
- 115: ds=771 sev=B
- 123: ds=754 sev=B
- 446: ds=731 sev=B
- 335: ds=695 sev=B
- 777: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=88 sev=blue
  - 33: ds=63 sev=purple
  - 88: ds=50 sev=purple
  - 00: ds=47 sev=purple
  - 55: ds=40 sev=purple
  - 66: ds=35 sev=purple
  - 44: ds=27 sev=purple
  - 22: ds=13 sev=-
  - 99: ds=8 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 89: ds=77 sev=red
  - 46: ds=74 sev=red
  - 28: ds=65 sev=red
  - 26: ds=49 sev=blue
  - 29: ds=41 sev=blue
  - 15: ds=37 sev=blue
  - 36: ds=35 sev=purple
  - 67: ds=32 sev=purple
  - 03: ds=31 sev=purple
  - 23: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:187, 26:184, 1:179, 16:121, 35:99, 33:79, 22:78, 29:75, 20:71, 23:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=187 fs=3 fl=2 hz=0.007741935483870969, 26:ds=184 fs=1 fl=0 hz=0.0049382716049382715, 1:ds=179 fs=3 fl=3 hz=0.00857843137254902, 16:ds=121 fs=2 fl=1 hz=0.009174311926605505, 35:ds=99 fs=0 fl=1 hz=0.00487012987012987, 33:ds=79 fs=21 fl=2 hz=0.026744186046511628, 22:ds=78 fs=44 fl=0 hz=0.04851157662624035, 29:ds=75 fs=17 fl=2 hz=0.02132435465768799, 20:ds=71 fs=22 fl=1 hz=0.02481121898597627, 23:ds=69 fs=17 fl=2 hz=0.021300448430493273

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S7: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=22 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=16), P2:4 (gap=31), P3:4 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=985 sev=B
- 668: ds=969 sev=B
- 166: ds=864 sev=B
- 378: ds=863 sev=B
- 666: ds=861 sev=B
- 455: ds=855 sev=B
- 225: ds=825 sev=B
- 279: ds=816 sev=B
- 111: ds=780 sev=B
- 222: ds=779 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=64 sev=purple
  - 88: ds=57 sev=purple
  - 22: ds=25 sev=purple
  - 66: ds=24 sev=-
  - 11: ds=19 sev=-
  - 33: ds=18 sev=-
  - 55: ds=13 sev=-
  - 77: ds=6 sev=-
  - 00: ds=4 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 04: ds=102 sev=red
  - 89: ds=65 sev=red
  - 45: ds=49 sev=blue
  - 46: ds=49 sev=blue
  - 15: ds=42 sev=blue
  - 01: ds=41 sev=blue
  - 13: ds=37 sev=blue
  - 69: ds=35 sev=purple
  - 59: ds=34 sev=purple
  - 35: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:633, 35:299, 32:250, 5:125, 14:105, 29:78, 15:67, 34:64, 27:48, 9:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=633 fs=4 fl=1 hz=0.0154320987654321, 35:ds=299 fs=1 fl=3 hz=0.008032128514056224, 32:ds=250 fs=3 fl=2 hz=0.00946372239747634, 5:ds=125 fs=18 fl=1 hz=0.02328288707799767, 14:ds=105 fs=39 fl=0 hz=0.04426787741203178, 29:ds=78 fs=18 fl=2 hz=0.023781212841854936, 15:ds=67 fs=15 fl=2 hz=0.019653179190751446, 34:ds=64 fs=19 fl=0 hz=0.023086269744835963, 27:ds=48 fs=19 fl=4 hz=0.02454642475987193, 9:ds=47 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=74 flags=purple
- S23: ds=67 flags=purple
- S20: ds=57 flags=purple
- S0: ds=56 flags=blue+purple
- S10: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 666 -> combined:829(B); evening:861(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:38(purple); midday:88(blue)
- 13 -> combined:41(blue); evening:37(blue)
- 15 -> combined:75(red); evening:42(blue); midday:37(blue)
- 22 -> combined:27(purple); evening:25(purple)
- 23 -> combined:30(purple); midday:29(purple)
- 33 -> combined:36(purple); midday:63(purple)
- 36 -> combined:36(purple); midday:35(purple)
- 44 -> combined:55(purple); evening:64(purple); midday:27(purple)
- 46 -> combined:98(red); evening:49(blue); midday:74(red)
- 49 -> combined:33(purple); evening:31(purple)
- 55 -> combined:26(purple); midday:40(purple)
- 66 -> combined:48(purple); midday:35(purple)
- 67 -> combined:28(purple); midday:32(purple)
- 88 -> combined:101(blue); evening:57(purple); midday:50(purple)
- 89 -> combined:130(red); evening:65(red); midday:77(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.867285714285714)[R1,Mirror-Echo], 6(2.4499285714285715)[R3,Mirror-Echo], 8(1.2672857142857143)[R1,Double-Pressure], 0(0.9079999999999999)[R2,Double-Pressure], 5(0.8716999999999999)[R2,Double-Pressure]
- P2: 4(6.89105)[R1,XVAR-Cons(CEM)], 3(2.9685714285714284)[R3,Mirror-Echo], 1(1.0971)[R2,Double-Pressure], 6(1.0971)[R2,Double-Pressure], 8(1.0502857142857143)[R2,Mirror-Echo]
- P3: 4(7.855071428571429)[R1,XVAR-Cons(CEM)], 6(6.4667)[R2,XVAR-Cons(CEM)], 3(6.303935714285714)[R3,XVAR-Cons(CEM)]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` (n=1000)
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state NorthCarolina4 --strict` → OK.
- Q2:
  - Positional pressure is coherent but points to a different dominant lane universe than the winners:
    - Combined top digits: `1/4/4`
    - Midday top digits: `8/3/3` (with a hard-due P3=3, ds=63)
- Q3:
  - Positional shortlist is dominated by the `144/146/143/134/...` lane family (strong 1/3/4/6 bias); the winners are not top candidates here.
- Q4:
  - Repeat watch indicates an active environment (Combined current_index=30; Midday current_index=28), but it does not directly explain winner indices 7 and 8.
- Q5:
  - VTRAC overlay overdue list is led by indices like 32/16/35/29; it does not elevate idx7 or idx8.
- Q6:
  - Doubles/pairs pressure is high (many sev=B doubles; repeating pairs like 88 are blue), supporting “busy” posture without narrowing to the winners.
- Q7:
  - Sums are broadly flagged (purple/red+purple) → low discrimination.
- Q8:
  - Blackapple is low signal (score=1) and does not directly isolate the winners; treat as context only.
- Q9:
  - Cross-variant pair alerts show strong persistence across variants; use this as environment context, not a direct caller.
- Q10:
  - Aux is best used here as a dominance/context meter (1/3/4/6 lanes), while the decisive evidence for the Evening win comes from Stable + Combined winners lens.

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
  - Primary hedge: `567` boxed set (because Hot Zones ranks the winner canonical very well: best rank 16).
  - Optional structural hedge: VTRAC idx7 family (8 straights) if you want a VT-straight overlay instead of pure box.
- Candidate universe (Evening):
  - Primary: `135` boxed set (Stable exact boxed/straight=True + Combined winners-lens on-board).
  - Optional near-lane hedge: `134` (Stable top compound rank 3) only if you explicitly allow 1-digit-adjacent expansion.
- Evidence vectors:
  - Midday: Hot Zones rank 16 + VTRAC idx7 moderate rank; Stable miss (so keep small).
  - Evening: Stable exact (scores/compound) + VTRAC idx8 moderate + Combined winners-lens `hit-winner` tagging.
- Coverage mapping + pack decision:
  - Recommended posture is “two small boxes” (567 for Midday, 135 for Evening) rather than broad lane spraying.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday: `567` box would have hit (winner 765).
  - Evening: `135` box would have hit (winner 153).
- Key tags:
  - Combined lens carries the Evening winner (literal 153 + hit-winner tags).
  - Hot Zones strongly supports the Midday winner (rank 16) even though Stable missed it.
- Drivers:
  - Evening win: Stable exact + VTRAC moderate + Combined-lens visibility.
  - Midday win: Hot Zones (family/VT lane) is the primary corroborator.
- Conflicts:
  - Hot Zones vs Stable disagreement (Midday vs Evening) is the key analytic tension; keep as a useful weighting example for later aggregation.
- Fix-now vs fix-later:
  - Fix-now: none (pipeline integrity checks passed).
  - Fix-later: quantify when “Combined-lens on-board” should override weak draw-specific ladder evidence.
- Next run:
  - Continue D=2025‑06‑22 run reports; keep this as a strong example of cross-variant (Combined) relevance.
