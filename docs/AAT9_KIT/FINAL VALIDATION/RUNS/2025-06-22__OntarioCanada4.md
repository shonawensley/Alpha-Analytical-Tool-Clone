# Master Validation Run Report — OntarioCanada4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/OntarioCanada4/`
- Winners lens: `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-06-22/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-06-22/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-06-22/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-06-22/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2025-06-22/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2025-06-22/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac16_winner_616_20251221_222132.html`
- `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_918_20251221_222130.html`

Winners JSON files:
- `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac16_winner_616_20251221_222132.json`
- `sharepacks/2025-06-22/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac24_winner_918_20251221_222130.json`

Part A answers (fill using the template’s Part A questions):
- Q1: Set1 ladder lanes are active but do not anchor the winners (both are largely off-board).
  - Set1/Draw1 ladders (from winners JSON; same in both winner files):
    - Midday: col1 ladders `094**`; col2 ladders `9467** / 9647** / 6794** / 7964**`
    - Evening: col1 ladders `922** / 229**`; col2 ladders `5922** / 2259** / 9225**`
    - Combined: col1 ladders `900** / 009**`; col2 ladders `5900** / 0059** / 0095**`
- Q2: Column persistence is high (repeated `094**`, `922**`, and `900/009` lanes), but that dominant lane story does not “narrate” either winner (918 / 616).
- Q3: “Last survivors” density is high, but winner tagging is limited and mostly indirect:
  - Winner presence in lens tags:
    - 918 (canon 189): `hit-winner` cells=2; literal substring cells=0; canonical substring cells=0.
    - 616 (canon 166): `hit-winner` cells=6; literal substring cells=0; canonical substring cells=0.
- Q4: Variant bias is clear in the board (0/9/4, 9/2, 0/9), but the winners are orthogonal:
  - Midday 918 (canon 189): not reflected in the dominant ladders.
  - Evening 616 (canon 166): also not reflected; only modest `hit-winner` tagging exists.
- Q5: Permutation lane clarity is high (very legible lane universes), but it points to non-winner structure → not an actionable winner-isolation day.
- Q6: Environment verdict: low-confidence day for direct prediction; treat as **pass/tiny hedge**.
- Q7: Hot Zones overlap is weak for both winners (best ranks 137 and 182; both `triad_present=False` in the winner_map snapshot).
- Q8: Cross-set carryover exists (board + Stable + DR emphasize `229/009/922/900`), but it does not resolve into the actual winners.
- Q9: Aux cues don’t align to the winners:
  - Positional top digits: Combined `9/8/2`, Midday `7/8/6`, Evening `1/3/9` (none match 918 or 616 cleanly).
  - Blackapple: score=2 with `pairs.remaining_count=0` and floating digits `3/9`, but top candidates do not include winners.
- Q10: 4 hit criteria viability (pre-results lens): low; treat this as a “skip posture” training example.
- Q11: Exact triple presence (winners lens):
  - 918 / canonical 189: literal substring cells=0; canonical substring cells=0; `hit-winner` cells=2.
  - 616 / canonical 166: literal substring cells=0; canonical substring cells=0; `hit-winner` cells=6.
- Q12: “Profitable environment” summary:
  - Strong lane dominance exists, but it’s the wrong lane → useful negative-control for “busy board ≠ correct board”.
- Q13: Dominance vs dilution:
  - Dominance exists (`094`, `922`, `900/009`), but it is not the winner universe → dilution relative to outcomes.
- Q14: Noise check:
  - High noise / wrong convergence; treat as a pass/tiny day.
  - Fix-later note: DR Evening winner overlay has 0 matches (items_total=0); treat as tool outcome, not missing artifacts (see Part 2.DR).

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — OntarioCanada4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — OntarioCanada4 (2025-06-22)

## Midday winner 918 (canonical 189)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=2 | family_rows=15 | exact_boxed=2 | exact_straight=2 | vt_boxed=2
- Scores (patterns_scores.csv): rank 4877, section Midday, Set Set3, Draw Draw1, Col 7, score 8.5, hot 0, vt_straight 0.0 | why straight|cov1|hidden3v|set_chain2
- Compound (patterns_compound.csv): rank 1243, section Midday, score 10.5, col1_hits 0, hot2 0, set_chain 2, draw_chain 0 | why set_chain2
- Families (patterns_families.csv): 13 rows contain digits; best rank 941, section Combined, score 11.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=134

## Evening winner 616 (canonical 166)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=6 | family_rows=517 | exact_boxed=6 | exact_straight=6 | vt_boxed=6
- Scores (patterns_scores.csv): rank 2543, section Midday, Set Set1, Draw Draw4, Col 3, score 13.0, hot 0, vt_straight 2.0 | why straight|cov1|hp_repeat2|mirror|double_mirror|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 417, section Midday, score 19.0, col1_hits 0, hot2 0, set_chain 1, draw_chain 3 | why draw_chain3|vstrx2|dblmirrorx5
- Families (patterns_families.csv): 60 rows contain digits; best rank 126, section Combined, score 24.5, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=3

## Top compound candidates (patterns_compound.csv)
- rank    2 | canon 009 | section Combined | score 96.0 | col1_hits 9 | hot2 11
- rank    1 | canon 229 | section Evening | score 100.0 | col1_hits 8 | hot2 11
- rank    5 | canon 005 | section Combined | score 70.0 | col1_hits 4 | hot2 8
- rank    8 | canon 099 | section Combined | score 68.0 | col1_hits 6 | hot2 8
- rank   11 | canon 0099 | section Combined | score 61.0 | col1_hits 6 | hot2 8
- rank   20 | canon 456 | section Midday | score 52.0 | col1_hits 5 | hot2 8
- rank    5 | canon 225 | section Evening | score 70.0 | col1_hits 1 | hot2 6
- rank   13 | canon 259 | section Evening | score 57.0 | col1_hits 1 | hot2 6
- rank   14 | canon 2259 | section Evening | score 55.0 | col1_hits 1 | hot2 6
- rank   33 | canon 459 | section Midday | score 44.5 | col1_hits 3 | hot2 6

## Top families (patterns_families.csv)
- rank 1146 | family 18 | score 8.0 | hot2 0 | section Midday
- rank  772 | family 14 | score 13.5 | hot2 0 | section Midday
- rank  634 | family 30 | score 15.0 | hot2 0 | section Midday
- rank  683 | family 14 | score 14.5 | hot2 0 | section Midday
- rank  876 | family 20 | score 12.0 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Both winners have exact boxed/straight=True in Stable, but both are very deep-ranked:
    - 918: scores rank 4877; compound rank 1243.
    - 616: scores rank 2543; compound rank 417.
- Q2: 4 hit criteria mapping
  - Midday (918): exact boxed/straight=True; VT boxed exists (vt_boxed_count=134) but it’s not a top-tier call.
  - Evening (616): exact boxed/straight=True; VT boxed exists (vt_boxed_count=3) but still deep-ranked.
- Q3: Winners output alignment
  - Stable spotlight/scores/compound/metrics are internally consistent; this is a true “weak hit / deep rank”, not missing artifacts.
- Q4: Dominance / noise
  - Stable’s top compound candidates are dominated by other canonicals (229/009/005/099…) rather than 189 or 166.
- Q5: Where the winners show up
  - Strong “post-results” spotlight presence exists (918: exact_canonical_rows=2; 616: exact_canonical_rows=6), but neither is competitive vs top compounds.
- Q6: Miss analysis
  - Not a hard miss (exact exists), but not actionable isolation (too deep).
- Q7: Validation checks (V)
  - Outputs present; no missing brain artifacts.
- Q8: Optimization notes
  - None now (avoid tuning from one state/day).
- Q9: Cross-tool synergy seed
  - Stable’s dominant canonicals (229/009) align with the winners-lens ladders (`922/229`, `900/009`) and with DR’s top patterns (`922/599`), even though the actual winners are elsewhere.
- Q10: Analyst’s extra insight
  - Stable is acting as a strong “environment map” here; the correct learning is “how to detect and skip when the environment converges away from winners”.

---

### 2.Digit Reduction — OntarioCanada4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20251222)

## Midday winner 918 (canonical 189)
- Stamp (winner_stamp.json): items_total=78 | exact_any=0 exact_final=0 | vtrac_any=78 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=78 | exact_any=0 vtrac_any=78 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=7 vt_straight=0
- Hits (winner_hits.csv): rows=78 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=7 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 616 (canonical 166)
- Stamp (winner_stamp.json): items_total=0 | exact_any=0 exact_final=0 | vtrac_any=0 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=0 | exact_any=0 vtrac_any=0 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=0 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True
- Coverage gaps: missing_flags, missing_hits

## Combined winner 918 (canonical 189)
- Stamp (winner_stamp.json): items_total=112 | exact_any=0 exact_final=0 | vtrac_any=112 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=16 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=112 | exact_any=0 vtrac_any=112 | drop_exact_any=0 drop_vtrac_any=16 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=17 vt_straight=0
- Hits (winner_hits.csv): rows=112 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=17 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 5 | pattern 922 | score_v2 13.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 922 | score_v2 13.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 3 | pattern 922 | score_v2 12.327143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set2 draw Draw1 col 2 | pattern 922 | score_v2 12.077143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 11.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 11.927143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 11.887143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 11.727143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 11.687143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 11.677143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 922 | score_v2 13.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Evening | best_pattern 922 | score_v2 12.327143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 599 | score_v2 11.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 940 | score_v2 11.61381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 592 | score_v2 11.477143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 559 | score_v2 11.427143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 922 | score_v2 11.377143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 592 | score_v2 11.077143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 559 | score_v2 11.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 559 | score_v2 10.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - DR does not isolate either winner as a top-candidate triad (`winner_triads_as_candidates=False` for both).
  - Midday 918: broad VTRAC-any coverage (vtrac_any=78), but no final hits.
  - Evening 616: 0 DR matches for this winner (items_total=0); flags/hits are header-only because there are no matched items.
- Q2: Stamp interpretation
  - Midday 918: vtrac_any=78 (very broad), vt_boxed=7 → “covered broadly”, not “narrowed”.
  - Evening 616: stamp/flags/hits indicate 0 matches; treat as a DR miss (tool outcome), not missing artifacts.
  - Combined 918: vtrac_any=112 (very broad), vt_boxed=17 → also broad.
- Q3: 4 hit criteria mapping
  - DR is registering VTRAC/drop signals, not producing a clean exact/boxed candidate set for these winners.
- Q4: Dominance / noise
  - Top per_item and top candidates emphasize `922`/`599` patterns (non-winner dominance), not 189/166.
- Q5: Where the winners show up
  - Midday/Combined show vtrac_any, but the winner is not a top candidate; Evening has 0 DR matches (items_total=0).
- Q6: Miss analysis
  - This is a practical DR miss (or “non-isolation”) for the winners; Evening has a clean 0-match overlay (items_total=0).
- Q7: Validation checks (V)
  - Fix-later: treat Evening 616 as a DR negative-control example (0 matches); do not label as missing artifacts.
- Q8: Optimization notes
  - None now; main caution is to interpret “0 matches” as tool outcome (not pipeline failure).
- Q9: Cross-tool synergy seed
  - DR’s dominant patterns (`922`/`599`) agree with Stable and the winners-lens board dominance (9/2/0 universe), reinforcing that the environment converged elsewhere.
- Q10: Analyst’s extra insight
  - DR is functioning as an environment detector on this day; it’s valuable evidence for skip/low-spend posture rather than direct candidate generation.

---

### 2.VTRAC Analyzer — OntarioCanada4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20251221_222526)

## Top indices (from enhanced JSON)
- index 5 | score 62.87287 | features: presence=47.45537, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 34 | score 54.85063999999999 | features: presence=30.43313999999999, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 33 | score 44.869105000000005 | features: presence=28.391605000000006, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 14 | score 40.6707325 | features: presence=24.073232500000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 15 | score 34.16630416666667 | features: presence=22.5021375, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 25 | score 22.918000000000003 | features: presence=13.820500000000001, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 22 | score 17.985125000000007 | features: presence=12.949500000000002, first_hit=0.33333333333333337, column_span=0.23229166666666665, persistence=0.4
- index 7 | score 17.72636666666667 | features: presence=9.65595, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 24 | score 14.823270000000003 | features: presence=6.585770000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 35 | score 13.616249999999999 | features: presence=4.47875, cross_section=0.5, set_echo=0.6, first_hit=0.2

## Top straights (from enhanced JSON)
934, 943, 590, 593, 059, 093, 345, 594, 095, 094

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 616 | index 16 | file OntarioCanada4_vtrac16_winner_616_20251221_222132.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 918 | index 24 | file OntarioCanada4_vtrac24_winner_918_20251221_222130.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 616 | index 16 rank 31/35 | score 0.0 | winner_in_index_straights=False | top_index_straights: (none)
- winner 918 | index 24 rank 9/35 | score 14.823270000000003 | winner_in_index_straights=False | top_index_straights: 364 (4.754), 963 (3.516), 986 (3.284)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - 918: index 24 ranks 9/35 (score ~14.8) → moderate presence but not in top straights.
  - 616: index 16 ranks 31/35 (score 0.0) → effectively absent.
- Q2: 4 hit criteria mapping
  - For both winners: `winner_in_index_straights=False` (top straights list does not contain winners).
- Q3: Winners output alignment
  - Outputs are consistent (winners lens identifies indices 24 and 16); the analyzer’s ranking simply doesn’t favor them.
- Q4: Dominance / noise
  - Top indices are 5/34/33/14/15…, not 24/16.
- Q5: Where the winners show up
  - 918 is “mid-tier” (rank 9/35); 616 is very weak (31/35).
- Q6: Miss analysis
  - Treat as a VTRAC analyzer miss day for both winners (especially 616).
- Q7: Validation checks (V)
  - Outputs present; no missing artifacts.
- Q8: Optimization notes
  - None now (avoid tuning).
- Q9: Cross-tool synergy seed
  - Aux VTRAC overdue list includes idx16 as highly overdue (ds=186), which matches the Evening winner’s index even though the VTRAC analyzer rank is poor → worth tracking across more days.
- Q10: Analyst’s extra insight
  - VTRAC analyzer here is not acting as a “winner isolator”; keep it as a contributor signal, not a primary decider, until we have more days.

---

### 2.Hot Zones — OntarioCanada4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2025-06-22)

## Midday winner 918 (canonical 189)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 137
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 616 (canonical 166)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 182
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 227 | vt_triad 33 | score_mean 22.372 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 277 | vt_triad 33 | score_mean 22.306 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 578 | vt_triad 134 | score_mean 21.485 | tags funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    4 | triad 267 | vt_triad 233 | score_mean 21.364 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 127 | vt_triad 233 | score_mean 21.021 | tags funnel_precol1,hot16,hot20,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 157 | vt_triad 123 | score_mean 20.718 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical5,vt_only_lane,vt_straight
- rank    7 | triad 334 | vt_triad 45 | score_mean 20.701 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 279 | vt_triad 335 | score_mean 20.209 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 678 | vt_triad 234 | score_mean 20.194 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank   10 | triad 009 | vt_triad 15 | score_mean 20.186 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - Both winners appear in top lanes, but only at weak ranks:
    - 918 best rank 137; 616 best rank 182.
  - Winner map is present but `triad_present=False` for both (top-20 snapshot limitation).
- Q2: 4 hit criteria mapping
  - Per-lane indicates has_straight=True and has_vt_straight=True, but ranks are too deep for strong isolation.
- Q3: Winners output alignment
  - “winner_not_in_winner_map” is expected when the winner rank is outside the top-20 (+guard) snapshot; do not treat as corruption.
- Q4: Dominance / noise
  - Hot Zones top lanes emphasize 227/277/… and include 009 in the top-10; not a clean story for 189/166.
- Q5: Where the winners show up
  - Deep ranks only (137 and 182).
- Q6: Miss analysis
  - Practical miss / weak corroboration day for Hot Zones.
- Q7: Validation checks (V)
  - Outputs present; no missing artifacts.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Hot Zones top lanes include `009` (rank 10), matching Stable’s top compound `009` and the Combined winners-lens ladder `009**` — strong non-winner convergence.
- Q10: Analyst’s extra insight
  - Hot Zones aligns with Stable on the “0/9 universe” but not on the actual winners; this is strong evidence for skip gating when multiple tools converge away from the outcomes.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Broad cross-tool agreement on a non-winner universe: `009/229/922/900` shows up in winners lens ladders, Stable top compounds, DR top patterns, Hot Zones top lanes, and Aux positional consensus notes.
- Conflicts/noise:
  - That strong convergence did not resolve into either winner (918/616).
  - Stable does have exact hits for both winners, but only at very deep ranks → low-confidence.
- Aggregator/aux hooks to test next:
  - Treat “multi-tool convergence away from winners” as a skip/low-spend posture candidate.
  - Fix-later: log Ontario Evening 616 as a DR 0-match negative-control (overlay exists; items_total=0) so it’s not confused with pipeline failure later.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=517, 678, 343, 211, 367
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=678, 211, 221, 847, 805
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=517, 343, 367, 875, 896

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=39 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=25), P2:8 (gap=30), P3:2 (gap=36)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 004: ds=835 sev=B
- 288: ds=828 sev=B
- 778: ds=809 sev=B
- 115: ds=802 sev=B
- 144: ds=793 sev=B
- 055: ds=771 sev=B
- 346: ds=745 sev=B
- 255: ds=728 sev=B
- 111: ds=718 sev=B
- 116: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=121 sev=red
  - 00: ds=93 sev=blue
  - 55: ds=74 sev=blue
  - 66: ds=58 sev=purple
  - 77: ds=44 sev=purple
  - 99: ds=25 sev=purple
  - 44: ds=19 sev=-
  - 22: ds=5 sev=-
  - 11: ds=3 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 35: ds=65 sev=red
  - 59: ds=56 sev=red
  - 26: ds=47 sev=blue
  - 24: ds=46 sev=blue
  - 25: ds=43 sev=blue
  - 79: ds=37 sev=blue
  - 27: ds=32 sev=purple
  - 39: ds=27 sev=purple
  - 02: ds=26 sev=purple
  - 29: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:689, 1:285, 6:117, 26:116, 13:110, 5:82, 16:66, 34:60, 28:59, 3:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=689 fs=0 fl=0 hz=0.0, 1:ds=285 fs=1 fl=1 hz=0.006172839506172839, 6:ds=117 fs=10 fl=4 hz=0.016726403823178016, 26:ds=116 fs=3 fl=2 hz=0.008174386920980927, 13:ds=110 fs=22 fl=0 hz=0.02631578947368421, 5:ds=82 fs=28 fl=0 hz=0.03571428571428571, 16:ds=66 fs=2 fl=0 hz=0.005605381165919282, 34:ds=60 fs=12 fl=4 hz=0.017185821697099892, 28:ds=59 fs=17 fl=2 hz=0.020255863539445626, 3:ds=43 fs=20 fl=1 hz=0.022629310344827586

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=96 flags=blue+purple
- S22: ds=56 flags=purple
- S6: ds=52 flags=red+purple
- S7: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': True}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,PAT
  - 016: score=2 tags=FLT,PAT
  - 017: score=2 tags=FLT,PAT
  - 018: score=2 tags=FLT,PAT
  - 019: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,PAT
  - 026: score=2 tags=FLT,PAT
  - 027: score=2 tags=FLT,PAT
  - 028: score=2 tags=FLT,PAT
  - 029: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=20 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:8 (gap=24), P3:6 (gap=25)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=954 sev=B
- 099: ds=904 sev=B
- 228: ds=801 sev=B
- 333: ds=784 sev=B
- 255: ds=751 sev=B
- 566: ds=727 sev=B
- 338: ds=721 sev=B
- 355: ds=716 sev=B
- 011: ds=694 sev=B
- 368: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=108 sev=red
  - 88: ds=60 sev=purple
  - 66: ds=58 sev=purple
  - 00: ds=46 sev=purple
  - 55: ds=42 sev=purple
  - 77: ds=29 sev=purple
  - 99: ds=12 sev=-
  - 44: ds=9 sev=-
  - 22: ds=2 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 17: ds=47 sev=blue
  - 57: ds=45 sev=blue
  - 59: ds=42 sev=blue
  - 37: ds=39 sev=blue
  - 16: ds=35 sev=purple
  - 34: ds=33 sev=purple
  - 23: ds=32 sev=purple
  - 35: ds=32 sev=purple
  - 27: ds=31 sev=purple
  - 24: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:344, 16:186, 1:142, 34:127, 27:103, 26:90, 10:72, 33:63, 13:60, 6:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=344 fs=1 fl=1 hz=0.0056603773584905665, 16:ds=186 fs=4 fl=0 hz=0.008450704225352114, 1:ds=142 fs=4 fl=2 hz=0.011976047904191617, 34:ds=127 fs=13 fl=3 hz=0.01909307875894988, 27:ds=103 fs=16 fl=2 hz=0.020202020202020204, 26:ds=90 fs=0 fl=4 hz=0.006150061500615006, 10:ds=72 fs=22 fl=1 hz=0.02561247216035635, 33:ds=63 fs=22 fl=1 hz=0.026047565118912798, 13:ds=60 fs=21 fl=3 hz=0.026402640264026403, 6:ds=58 fs=18 fl=1 hz=0.02065217391304348

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=95 flags=blue+purple
- S3: ds=87 flags=purple
- S6: ds=74 flags=purple
- S2: ds=70 flags=purple
- S9: ds=46 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 069: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 159: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 348: score=3 tags=FLT,RS
  - 357: score=3 tags=FLT,RS
  - 789: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 024: score=2 tags=RS
  - 078: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=24 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:3 (gap=29), P3:9 (gap=24)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=985 sev=B
- 228: ds=931 sev=B
- 337: ds=898 sev=B
- 145: ds=853 sev=B
- 016: ds=834 sev=B
- 066: ds=831 sev=B
- 777: ds=819 sev=B
- 388: ds=805 sev=B
- 588: ds=772 sev=B
- 227: ds=720 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=89 sev=blue
  - 11: ds=50 sev=purple
  - 00: ds=48 sev=purple
  - 55: ds=37 sev=purple
  - 66: ds=29 sev=purple
  - 22: ds=27 sev=purple
  - 99: ds=24 sev=-
  - 77: ds=22 sev=-
  - 44: ds=14 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 12: ds=107 sev=red
  - 26: ds=67 sev=red
  - 35: ds=37 sev=blue
  - 06: ds=34 sev=purple
  - 03: ds=32 sev=purple
  - 39: ds=30 sev=purple
  - 59: ds=28 sev=purple
  - 25: ds=27 sev=purple
  - 05: ds=26 sev=purple
  - 79: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:675, 35:233, 6:196, 28:168, 1:148, 20:118, 3:115, 17:101, 26:58, 13:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=675 fs=1 fl=2 hz=0.009433962264150943, 35:ds=233 fs=0 fl=3 hz=0.005657708628005658, 6:ds=196 fs=14 fl=2 hz=0.02077922077922078, 28:ds=168 fs=7 fl=0 hz=0.011335012594458438, 1:ds=148 fs=0 fl=0 hz=0.0, 20:ds=118 fs=18 fl=1 hz=0.02280912364945978, 3:ds=115 fs=16 fl=3 hz=0.023199023199023196, 17:ds=101 fs=17 fl=3 hz=0.022753128555176336, 26:ds=58 fs=3 fl=2 hz=0.007552870090634441, 13:ds=55 fs=23 fl=2 hz=0.02969121140142518

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S25: ds=89 flags=purple
- S27: ds=79 flags=blue+purple
- S19: ds=77 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 1}}
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
- 228 -> evening:931(B); midday:801(B)
- 255 -> combined:728(B); midday:751(B)
- 288 -> combined:828(B); midday:954(B)
- 338 -> evening:675(B); midday:721(B)
- 388 -> combined:689(B); evening:805(B)
- 778 -> combined:809(B); evening:985(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:93(blue); evening:48(purple); midday:46(purple)
- 24 -> combined:46(blue); midday:30(purple)
- 25 -> combined:43(blue); evening:27(purple)
- 26 -> combined:47(blue); evening:67(red)
- 27 -> combined:32(purple); midday:31(purple)
- 35 -> combined:65(red); evening:37(blue); midday:32(purple)
- 39 -> combined:27(purple); evening:30(purple)
- 55 -> combined:74(blue); evening:37(purple); midday:42(purple)
- 59 -> combined:56(red); evening:28(purple); midday:42(blue)
- 66 -> combined:58(purple); evening:29(purple); midday:58(purple)
- 77 -> combined:44(purple); midday:29(purple)
- 79 -> combined:37(blue); evening:25(purple)
- 88 -> combined:121(red); evening:89(blue); midday:60(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(7.177314285714285)[R1,XVAR-Cons(CEM)], 1(5.847642857142858)[R3,XVAR-Cons(CEM)], 7(3.5214285714285714)[R2,XVAR-Cons(CM)], 4(0.34959999999999997)[R3,Mirror-Echo]
- P2: 5(6.809900000000001)[R2,XVAR-Cons(CEM)], 8(6.378107142857143)[R1,Mirror-Echo], 3(3.0698928571428574)[R3,Mirror-Echo], 6(0.1774857142857143)[R3,Swap]
- P3: 2(7.6777999999999995)[R1,XVAR-Cons(CEM)], 9(3.9742142857142855)[R2,Mirror-Echo], 4(2.3325285714285715)[R3,Mirror-Echo], 6(1.3464285714285715)[R1,Double-Pressure], 3(0.2746642857142857)[R3,Swap]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Draw snapshot provenance:
    - combined: `sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` (n=1000)
  - Workbook provenance: `data/history/Pick3StatsC4_2025-06-21.xlsm` (aux_state_label=Ontario).
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state OntarioCanada4 --strict` → OK.
- Q2:
  - Positional pressure is coherent internally, but does not match the winners:
    - Combined top digits: `9/8/2`
    - Midday top digits: `7/8/6`
    - Evening top digits: `1/3/9`
- Q3:
  - Positional shortlist is dominated by `952/982/959/...` lanes; neither 918 nor 616 appears as a top positional candidate.
- Q4:
  - Repeat watch is “active” but not explanatory for the winners’ indices:
    - Combined current_index=7; Midday current_index=21; Evening current_index=7.
- Q5:
  - VTRAC overlay is interesting for idx16 (Evening winner 616’s index):
    - top overdue indices include idx16 (ds=186), but idx24 is not near the top overdue list.
- Q6:
  - Doubles/pairs pressure is high (many sev=B doubles; lots of repeating pairs), but it doesn’t narrow to the winners.
- Q7:
  - Sums are broadly flagged (mostly purple / red+purple) → low discrimination for these outcomes.
- Q8:
  - Blackapple score is moderate (score=2; pairs_remaining=0), but top candidates do not include the winners; treat as context only.
- Q9:
  - Cross-variant alerts show multi-variant doubles/pairs pressure, reinforcing a “busy environment” posture (not a direct call).
- Q10:
  - Use Aux here primarily to corroborate “dominant lane universes” (0/9/2/4 and positional consensus) and record this as a miss day for the winners.

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
  - Default posture: pass/tiny (no coherent convergence on `189`).
  - If forced to act on board dominance: a small box-leaning universe around the visible lanes (`094`, `229`, `009`) is the most coherent “environment” hedge, but it would miss the actual Midday winner (918).
- Candidate universe (Evening):
  - Default posture: pass/tiny (no coherent convergence on `166`).
  - If forced: same board-dominance hedge (`922/229/009`) is the smallest coherent idea, but it would miss 616.
- Evidence vectors:
  - Pro: Stable has exact boxed/straight=True for both winners (post-results), and winners-lens `hit-winner` tags exist.
  - Contra: all primary “environment narratives” converge on `0/9/2/4` structure, not 918/616.
- Coverage mapping + pack decision:
  - Recommend pass/tiny posture; if you play, keep it to very small box hedges only (avoid broad spend on a “busy but wrong” day).

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Any “board dominance” pack (094/229/009/922) would miss the actual winners (918/616).
  - A post-hoc minimal “winner capture” hedge would be `189` boxed and `166` boxed, but the pre-results evidence for those was weak (deep ranks).
- Key tags:
  - Strong lane dominance (`094`, `922`, `900/009`) + heavy cross-variant positional consensus notes.
  - Blackapple pairs_remaining=0 (context), but no direct winner inclusion.
- Drivers:
  - Tools agree on a loud environment, but the outcomes land off-board.
- Conflicts:
  - Strong multi-tool convergence on non-winner structure vs actual winners.
- Fix-now vs fix-later:
  - Fix-now: none (alignment guard passes).
  - Fix-later: DR Evening overlay for Ontario 616 is a 0-match negative-control (items_total=0); do not treat as missing artifacts.
- Next run:
  - Continue D=2025‑06‑22 reports (Pennsylvania4 next); keep OntarioCanada4 as a negative-control “busy board, off-board winners” case.
