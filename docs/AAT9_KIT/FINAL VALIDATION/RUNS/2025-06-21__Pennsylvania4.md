# Master Validation Run Report — Pennsylvania4 — results 2025-06-21 (history workbook ~ 2025-06-20)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-21/Pennsylvania4/`
- Winners lens: `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2025-06-21/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2025-06-21/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2025-06-21/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2025-06-21/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2025-06-21/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2025-06-21/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251201_233404.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_081814.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_133333.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_134137.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251209_181938.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251219_164416.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251201_233404.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_081815.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_133333.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_134138.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251209_181939.html`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251219_164417.html`

Winners JSON files:
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_081814.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_133333.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251206_134137.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251209_181938.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251219_164416.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_081815.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_133333.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251206_134138.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251209_181939.json`
- `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251219_164417.json`

Part A answers (fill using the template’s Part A questions):
- Primary files used (latest stamp):
  - `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251219_164416.html`
  - `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_667_20251219_164416.json`
  - `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251219_164417.html`
  - `sharepacks/2025-06-21/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac8_winner_360_20251219_164417.json`

- Q1:
  - Set1 col1 ladders are hot/dense but do not tightly “advertise” either winner as a clean survivor lane.
  - Midday winner 667 has some `hit-winner` tagging (12 total cells), but it does not appear as an explicit `667` cell value.
  - Evening winner 360 (canonical 036) is essentially absent from the winners lens (1 `hit-winner` tagged cell total) and does not appear as an explicit `360/036` cell value.
- Q2:
  - Col1/col2 persistence is strong for other dominant clusters, but not for the winners’ literal/canonical forms.
- Q3:
  - Last-survivor story (from winners JSON digests):
    - Midday idx17: winner 667 has 0; the highest-occurrence family members are low-count (`117`, `662`, `711` with occ=1).
    - Evening idx8: environment is dominated by `013` (occ=18, pers=48), then `068`, `018`, `810`; winner canonical `036` has 0.
- Q4:
  - Variant bias: weak-to-mixed.
    - Midday: tool evidence later is stronger than the winners lens (Stable isolates 667 well even though the VTRAC winners stats show 0 occurrence).
    - Evening: winner is not carried strongly by the winners lens.
- Q5:
  - Perm lane clarity is low for both: neither `667` nor `360/036` appears as explicit cell values in the winners tables.
- Q6:
  - Environment verdict: **mixed** (Midday is tool-friendly; Evening is noisy/weak by winners lens).
- Q7:
  - Hot Zones overlap is weak for both winners (both are present but low-ranked in top_lanes; neither appears in the top20 winner map).
- Q8:
  - Cross-set carryover is strong for `013/068` style clusters (Evening family dominance), but not for the winners.
- Q9:
  - Aux-visible cues exist for the Evening winner canonical:
    - `036` appears as a due double candidate in Aux (Combined doubles list) and is the Evening winner canonical.
- Q10:
  - 4-hit-criteria viability:
    - Midday 667: Exact boxed is plausible if the tool stack elevates it (Stable does).
    - Evening 036: Exact boxed is plausible as a due-double/box play; VT-straight/VT-boxed is not strongly supported by VTRAC analyzer.
- Q11:
  - Exact triple presence in string tables:
    - `667` is not present as an explicit cell value in the winners lens.
    - `360/036` is not present as an explicit cell value in the winners lens.
- Q12:
  - Profitable environment summary:
    - Midday has strong Stable confirmation (even if the winners lens is not clean).
    - Evening is a classic “dominant other-family day” (013/068/018/810 dominate), so winner is not a clean survivor.
- Q13:
  - Dominance vs dilution:
    - Midday winner family is diluted (no clear dominance in the winners stats tables).
    - Evening is dominated by 013/068 clusters, not by 036.
- Q14:
  - Noise check: overall noisy; treat Evening as “high uncertainty” without strong convergence.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — Pennsylvania4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2025-06-21)

## Midday winner 667 (canonical 667)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=12 | family_rows=380 | exact_boxed=12 | exact_straight=12 | vt_boxed=12
- Scores (patterns_scores.csv): rank 160/4489 (rank_frac 0.035642682111828916) | score 21.5 (top 37.0, ratio 0.581081081081081, delta 15.5) | section Midday, Set Set1, Draw Draw4, Col 1, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat4|hot2|hidden3v|double_mirror|vtrac_straight|set_chain2|draw_chain4
- Compound (patterns_compound.csv): rank 17/1653 (rank_frac 0.0102843315184513) | score 48.5 (top 77.5, ratio 0.6258064516129033, delta 29.0) | section Midday, col1_hits 4, hot2 4, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|col1x4|hot1x1|hot2x4|vstrx9|dblmirrorx11
- Families (patterns_families.csv): count 67 | rank 18/1364 (rank_frac 0.013196480938416423) | score 27.0 (top 31.0, ratio 0.8709677419354839, delta 4.0) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=11

## Evening winner 360 (canonical 036)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=51 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 4466/4489 (rank_frac 0.9948763644464246) | score 6.0 (top 37.0, ratio 0.16216216216216217, delta 31.0) | section Evening, Set Set1, Draw Draw1, Col 7, hot 0, vt_straight 0.0 | why straight|cov1
- Compound (patterns_compound.csv): rank 1637/1653 (rank_frac 0.9903206291591047) | score 6.5 (top 77.5, ratio 0.08387096774193549, delta 71.0) | section Evening, col1_hits 0, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1
- Families (patterns_families.csv): count 24 | rank 516/1364 (rank_frac 0.3782991202346041) | score 16.5 (top 31.0, ratio 0.532258064516129, delta 14.5) | section Midday, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=81

## Top compound candidates (patterns_compound.csv)
- rank    5 | canon 038 | section Evening | score 63.0 | col1_hits 6 | hot2 8
- rank    4 | canon 229 | section Midday | score 68.0 | col1_hits 6 | hot2 8
- rank    8 | canon 228 | section Midday | score 60.5 | col1_hits 3 | hot2 7
- rank    9 | canon 338 | section Evening | score 56.5 | col1_hits 5 | hot2 6
- rank   11 | canon 133 | section Evening | score 54.0 | col1_hits 5 | hot2 6
- rank   12 | canon 01338 | section Evening | score 51.5 | col1_hits 4 | hot2 6
- rank   14 | canon 1338 | section Evening | score 49.5 | col1_hits 5 | hot2 6
- rank   17 | canon 678 | section Midday | score 48.5 | col1_hits 3 | hot2 6
- rank   30 | canon 0338 | section Evening | score 44.5 | col1_hits 5 | hot2 6
- rank   33 | canon 013 | section Evening | score 43.5 | col1_hits 4 | hot2 6

## Top families (patterns_families.csv)
- rank 1364 | family 2 | score 3.0 | hot2 0 | section Midday
- rank 1360 | family 19 | score 4.0 | hot2 0 | section Midday
- rank  126 | family 28 | score 22.0 | hot2 3 | section Midday
- rank  676 | family 20 | score 14.5 | hot2 1 | section Midday
- rank  885 | family 24 | score 12.5 | hot2 1 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Midday winner 667 is strongly present in Stable brain outputs:
    - Scores rank 160/4489 (~3.6%), Set1 Draw4 Col1, hot2=2, vt_straight=2.0.
    - Compound rank 17/1653 (~1.0%), with strong col1_hits/hot2 and chain evidence.
  - Evening winner 036 is present but buried:
    - Scores rank 4466/4489 (~99.5%), low score, weak compound.
- Q2:
  - Midday: exact boxed/straight is viable (Stable exact flags True, and the winner is high ranked).
  - Evening: exact viability exists only in a “box it because it exists” sense; Stable does not elevate it.
- Q3:
  - Stable winners artifacts align with metrics (`validate_stable_winners.py` passes).
- Q4:
  - Midday is relatively clean in Stable; Evening is noisy with many competing clusters.
- Q5:
  - Top compound clusters include `038`, `338`, `133`, `013/0338` families (dominant in Evening), while Midday has the winner elevated directly.
- Q6:
  - Miss analysis (Evening): winner `036` lacks reinforcing hot/chain signals and is not prioritized.
- Q7:
  - (V) Data/schema OK; artifacts present; strict tables↔aux alignment passed.
- Q8:
  - Optimization note (log-only): consider whether “due-double evidence” should boost low-ranked but present Stable rows like 036 (only as a controlled overlay, not a global weight).
- Q9:
  - Cross-tool synergy seed: use Stable as the primary “caller” for Midday here; Evening likely requires Aux confirmation (doubles/pairs) to justify any coverage.
- Q10:
  - Extra: Pennsylvania shows a clear Midday/evening asymmetry: Stable can be strong on one draw and nearly useless on the other.

---

### 2.Digit Reduction — Pennsylvania4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20251219)

## Midday winner 667 (canonical 667)
- Stamp (winner_stamp.json): items_total=172 | exact_any=120 exact_final=0 | vtrac_any=172 vtrac_final=0 | drop_exact_any=6 drop_exact_final=0 | drop_vtrac_any=121 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=172 | exact_any=120 vtrac_any=172 | drop_exact_any=6 drop_vtrac_any=121 | family_exact_any=0 family_vtrac_any=9 | vt_boxed=135 vt_straight=0
- Hits (winner_hits.csv): rows=172 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=135 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.577143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Evening winner 360 (canonical 036)
- Stamp (winner_stamp.json): items_total=204 | exact_any=0 exact_final=0 | vtrac_any=202 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=51 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=15 family_vtrac_final=0
- Flags (winner_flags.csv): rows=204 | exact_any=0 vtrac_any=202 | drop_exact_any=0 drop_vtrac_any=51 | family_exact_any=0 family_vtrac_any=15 | vt_boxed=36 vt_straight=0
- Hits (winner_hits.csv): rows=204 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=36 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=40 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=10.864643 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 667 (canonical 667)
- Stamp (winner_stamp.json): items_total=236 | exact_any=132 exact_final=0 | vtrac_any=236 vtrac_final=0 | drop_exact_any=6 drop_exact_final=0 | drop_vtrac_any=122 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=236 | exact_any=132 vtrac_any=236 | drop_exact_any=6 drop_vtrac_any=122 | family_exact_any=0 family_vtrac_any=9 | vt_boxed=139 vt_straight=0
- Hits (winner_hits.csv): rows=236 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=139 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=16 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=11.777143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 990 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 599 | score_v2 10.958571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 003 | score_v2 10.864643 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 599 | score_v2 10.837143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 2 | pattern 922 | score_v2 10.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 599 | score_v2 10.558571 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 3 | pattern 922 | score_v2 10.327143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 7 | pattern 599 | score_v2 10.308571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 599 | score_v2 10.277143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw7 col 1 | pattern 599 | score_v2 10.220476 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 990 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 599 | score_v2 10.958571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 003 | score_v2 10.864643 | tags exact,vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 922 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 599 | score_v2 10.308571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 10.208571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 599 | score_v2 10.158571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 228 | score_v2 10.064643 | tags exact,vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 922 | score_v2 9.737143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 992 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - DR does not surface either winner as a top candidate (`winner_present=False` for both Midday and Evening top candidates), despite large exact_any/vtrac_any coverage counts.
- Q2:
  - Practical DR read: it is a “coverage detector” here (vt_boxed high), not a winner caller (no top-candidate hit).
- Q3:
  - DR winners artifacts are internally consistent (`validate_dr_winners.py` passes).
- Q4:
  - Dominance inside DR is on patterns like `990/599/003/922`, not on either winner.
- Q5:
  - Top candidates: `990`, `599`, `003`, `922` dominate the score list.
- Q6:
  - Miss analysis: winner may be present in the broader reducer space but not promoted into top candidates.
- Q7:
  - (V) Schema/data OK; stamp↔flags↔hits consistent.
- Q8:
  - Optimization note (log-only): if DR is intended to be actionable, it likely needs a different “top candidates” extraction mode for triples/doubles days.
- Q9:
  - Cross-tool synergy seed: DR top candidates align more with Stable’s Evening compound dominance (003/013/038 lanes), reinforcing that Evening was “013/038-family driven”.
- Q10:
  - Extra: DR is useful here primarily as a coverage sanity layer, not a direct caller.

---

### 2.VTRAC Analyzer — Pennsylvania4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20251219_165155)

## Top indices (from enhanced JSON)
- index 27 | score 66.34507749999997 | features: presence=46.637577499999985, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 11 | score 43.5571875 | features: presence=26.509687500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 29 | score 40.001407500000006 | features: presence=25.283907500000005, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 10 | score 39.375189166666665 | features: presence=25.781022500000006, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 4 | score 25.141916666666674 | features: presence=18.031500000000005, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 13 | score 23.016137499999996 | features: presence=13.848637499999997, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 22.624785000000003 | features: presence=16.007285, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 7 | score 21.193535 | features: presence=12.456035000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 3 | score 20.949525 | features: presence=11.273900000000001, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 20 | score 17.185250000000003 | features: presence=10.127750000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
208, 287, 782, 872, 832, 082, 203, 703, 037, 032

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 667 | index 17 | file Pennsylvania4_vtrac17_winner_667_20251219_164416.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 360 | index 8 | file Pennsylvania4_vtrac8_winner_360_20251219_164417.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 667 | index 17 rank 16/35 (rank_frac 0.45714285714285713) | score 6.165958333333333 (top 66.34507749999997, ratio 0.09293769132055556, delta 60.17911916666664) | winner_in_index_straights=False | top_index_straights: 617 (1.266), 167 (1.245), 162 (0.69)
- winner 360 | index 8 rank 7/35 (rank_frac 0.2) | score 22.624785000000003 (top 66.34507749999997, ratio 0.3410167845534586, delta 43.72029249999997) | winner_in_index_straights=False | top_index_straights: 018 (9.652), 013 (7.457), 810 (6.481)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Winner indices:
    - Midday 667 (idx17) is weak (rank 16/35).
    - Evening 360 (idx8) is moderately supported (rank 7/35).
- Q2:
  - VT-straight is weak for both (`winner_in_index_straights=False`).
  - VT-boxed is not clearly justified from the day-level rankings for Midday; for Evening it’s “possible” but not a top-ranked call.
- Q3:
  - Winners lens agrees: Evening family dominance is on `013/068/018/810`, not on `036`.
- Q4:
  - VTRAC analyzer’s top indices (27/11/29/10/4/13/8/7/3/20) do not match Midday winner idx17; Evening idx8 is present in the top indices list but not dominant.
- Q5:
  - Use VTRAC here more as “day context” than a direct win caller; it does not isolate Midday 667 at all.
- Q6:
  - Miss analysis: Midday winner is off the top-index lane; Evening winner is in a moderately supported index but not in the straight shortlist.
- Q7:
  - (V) VTRAC artifacts exist and are non-empty.
- Q8:
  - Optimization note (log-only): for Evening, consider whether “dominant family stats (013) + due double (036)” should be treated as conflicting signals that cause a pass.
- Q9:
  - Cross-tool synergy seed: treat VTRAC as secondary confirmation only when it agrees with Stable/Hot Zones; it does not here for Midday.
- Q10:
  - Extra: VTRAC is a strong illustration of why we need cross-tool stacking — a mid-ranked index (idx8) can still host the winner, but doesn’t become actionable alone.

---

### 2.Hot Zones — Pennsylvania4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2025-06-21)

## Midday winner 667 (canonical 667)
- Top lanes (hot_zones_top_lanes.csv): present | rank 157/212 (rank_frac 0.7405660377358491) | score_mean 15.264 (top 22.783, ratio 0.6699732256507044, delta 7.519000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Evening winner 360 (canonical 036)
- Top lanes (hot_zones_top_lanes.csv): present | rank 142/212 (rank_frac 0.6698113207547169) | score_mean 15.538 (top 22.783, ratio 0.6819997366457446, delta 7.245000000000001)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 22.783 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    1 | triad 227 | vt_triad 33 | score_mean 22.783 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 459 | vt_triad 155 | score_mean 22.718 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    4 | triad 000 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    5 | triad 011 | vt_triad 12 | score_mean 20.667 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    6 | triad 003 | vt_triad 14 | score_mean 20.633 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 056 | vt_triad 112 | score_mean 20.347 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 267 | vt_triad 233 | score_mean 20.167 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    8 | triad 127 | vt_triad 233 | score_mean 20.167 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank   10 | triad 466 | vt_triad 25 | score_mean 19.8 | tags hot16,hot8,literal_draw,set1_bonus,straight_lane,vertical1,vertical3,vertical5,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Both winners are present in Hot Zones `top_lanes`, but at very low ranks:
    - 667 rank 157/212; 036 rank 142/212.
- Q2:
  - Lane structure exists (has_straight=True and has_vt_straight=True), but the winners are not dominant lanes.
- Q3:
  - Validation OK: `validate_hot_zones_winners.py` confirms winners present in top_lanes.
- Q4:
  - Noise: both winners are diluted (not top-lane; not in winner_map top20).
- Q5:
  - Dominant Hot Zones lanes are `277/227/459/000/011/003/056/...` (not winners).
- Q6:
  - Miss analysis: Hot Zones is not a useful “caller” here; it would require additional gating.
- Q7:
  - (V) Artifacts exist; schema OK.
- Q8:
  - Optimization note (log-only): verify whether Hot Zones winner_map top20 should remain strict; days like this suggest many hits occur outside the top20.
- Q9:
  - Cross-tool synergy seed: Hot Zones provides little support for either winner; lean on Stable/Aux instead.
- Q10:
  - Extra: Pennsylvania demonstrates a mismatch where Stable can isolate Midday even when Hot Zones does not, suggesting Hot Zones is not always the best confirmation layer.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Evening environment is consistently dominated by `013/038` family clusters across Stable/DR/VTRAC winners stats, not by the actual Evening winner canonical `036`.
  - Midday is primarily a Stable-driven win isolation case (667 is high-ranked in Stable).
- Conflicts/noise:
  - Hot Zones does not support either winner strongly (both are very low-ranked), while Stable strongly supports Midday 667.
- Aggregator/aux hooks to test next:
  - Consider a rule: when Stable is strong but Hot Zones is very weak, treat Hot Zones as non-required confirmation (avoid false “it must be hot-zones too” gating).
  - For Evening, treat due-double cues (036 is due in Aux) as a candidate-level boost only if at least one string-table tool surfaces it above a minimum threshold.

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-21/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=226, 354, 846, 041, 567
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=354, 041, 954, 578, 413
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=226, 846, 567, 917, 605

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=119 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=23), P2:3 (gap=39), P3:2 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=872 sev=B
- 012: ds=856 sev=B
- 455: ds=800 sev=B
- 467: ds=730 sev=B
- 059: ds=711 sev=B
- 244: ds=700 sev=B
- 036: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=49 sev=purple
  - 77: ds=47 sev=purple
  - 00: ds=42 sev=purple
  - 44: ds=41 sev=purple
  - 11: ds=19 sev=-
  - 88: ds=16 sev=-
  - 66: ds=15 sev=-
  - 33: ds=11 sev=-
  - 99: ds=10 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 15: ds=49 sev=blue
  - 38: ds=48 sev=blue
  - 39: ds=39 sev=blue
  - 03: ds=34 sev=purple
  - 23: ds=33 sev=purple
  - 37: ds=30 sev=purple
  - 07: ds=29 sev=purple
  - 18: ds=27 sev=purple
  - 47: ds=25 sev=purple
  - 27: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:253, 26:184, 1:152, 32:147, 4:136, 35:110, 6:82, 33:66, 5:63, 27:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=253 fs=3 fl=2 hz=0.008241758241758242, 26:ds=184 fs=0 fl=1 hz=0.005649717514124294, 1:ds=152 fs=5 fl=3 hz=0.010126582278481013, 32:ds=147 fs=2 fl=1 hz=0.005738880918220947, 4:ds=136 fs=20 fl=1 hz=0.02530120481927711, 35:ds=110 fs=2 fl=0 hz=0.005917159763313609, 6:ds=82 fs=20 fl=0 hz=0.021953896816684963, 33:ds=66 fs=20 fl=1 hz=0.02260495156081808, 5:ds=63 fs=13 fl=2 hz=0.01714898177920686, 27:ds=61 fs=18 fl=3 hz=0.023127753303964757

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=67 flags=purple
- S7: ds=61 flags=purple
- S19: ds=47 flags=purple
- S22: ds=46 flags=purple

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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=65 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=15), P2:3 (gap=19), P3:7 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=997 sev=B
- 118: ds=833 sev=B
- 559: ds=782 sev=B
- 018: ds=770 sev=B
- 288: ds=769 sev=B
- 255: ds=740 sev=B
- 668: ds=722 sev=B
- 199: ds=670 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=24 sev=-
  - 77: ds=23 sev=-
  - 00: ds=22 sev=-
  - 22: ds=21 sev=-
  - 44: ds=20 sev=-
  - 88: ds=13 sev=-
  - 11: ds=9 sev=-
  - 99: ds=8 sev=-
  - 66: ds=7 sev=-
  - 33: ds=5 sev=-
- non_repeating:
  - 48: ds=66 sev=red
  - 25: ds=65 sev=red
  - 68: ds=49 sev=blue
  - 29: ds=48 sev=blue
  - 69: ds=45 sev=blue
  - 28: ds=44 sev=blue
  - 19: ds=43 sev=blue
  - 17: ds=38 sev=blue
  - 03: ds=37 sev=blue
  - 37: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:596, 26:180, 4:173, 1:165, 6:160, 29:132, 16:126, 25:100, 32:73, 12:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=596 fs=6 fl=1 hz=0.01881720430107527, 26:ds=180 fs=1 fl=0 hz=0.0028328611898017, 4:ds=173 fs=18 fl=2 hz=0.026075619295958277, 1:ds=165 fs=2 fl=3 hz=0.00904977375565611, 6:ds=160 fs=16 fl=1 hz=0.0228494623655914, 29:ds=132 fs=23 fl=0 hz=0.030666666666666665, 16:ds=126 fs=2 fl=5 hz=0.008728179551122194, 25:ds=100 fs=20 fl=2 hz=0.024608501118568233, 32:ds=73 fs=6 fl=1 hz=0.008781558726673985, 12:ds=64 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=87 flags=purple
- S26: ds=79 flags=blue+purple
- S1: ds=78 flags=blue+purple
- S23: ds=74 flags=purple
- S22: ds=61 flags=purple
- S14: ds=35 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 024: score=3 tags=FLT,RS
  - 069: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 168: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 267: score=3 tags=FLT,RS
  - 456: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 078: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=37 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:5 (gap=39), P3:2 (gap=42)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=908 sev=B
- 788: ds=870 sev=B
- 557: ds=849 sev=B
- 779: ds=843 sev=B
- 278: ds=789 sev=B
- 444: ds=778 sev=B
- 899: ds=775 sev=B
- 778: ds=758 sev=B
- 009: ds=736 sev=B
- 077: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=112 sev=red
  - 55: ds=64 sev=purple
  - 33: ds=42 sev=purple
  - 66: ds=30 sev=purple
  - 44: ds=28 sev=purple
  - 00: ds=21 sev=-
  - 11: ds=14 sev=-
  - 88: ds=8 sev=-
  - 99: ds=5 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 59: ds=64 sev=red
  - 07: ds=56 sev=red
  - 49: ds=55 sev=blue
  - 78: ds=48 sev=blue
  - 23: ds=36 sev=purple
  - 39: ds=33 sev=purple
  - 15: ds=32 sev=purple
  - 89: ds=31 sev=purple
  - 47: ds=28 sev=purple
  - 12: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:422, 3:261, 16:209, 28:149, 26:92, 15:80, 1:76, 17:71, 4:68, 5:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=422 fs=0 fl=1 hz=0.004405286343612335, 3:ds=261 fs=12 fl=2 hz=0.020710059171597635, 16:ds=209 fs=4 fl=4 hz=0.011142061281337047, 28:ds=149 fs=15 fl=3 hz=0.02120141342756184, 26:ds=92 fs=2 fl=0 hz=0.005242463958060288, 15:ds=80 fs=35 fl=0 hz=0.042682926829268296, 1:ds=76 fs=8 fl=3 hz=0.013480392156862744, 17:ds=71 fs=24 fl=1 hz=0.02824858757062147, 4:ds=68 fs=28 fl=1 hz=0.03125, 5:ds=64 fs=15 fl=4 hz=0.020496224379719524

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=58 flags=purple
- S7: ds=52 flags=purple
- S9: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:711(B); evening:715(B)
- 255 -> evening:694(B); midday:740(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:34(purple); midday:37(blue)
- 07 -> combined:29(purple); evening:56(red)
- 15 -> combined:49(blue); evening:32(purple)
- 23 -> combined:33(purple); evening:36(purple)
- 37 -> combined:30(purple); midday:29(purple)
- 38 -> combined:48(blue); midday:28(purple)
- 39 -> combined:39(blue); evening:33(purple)
- 44 -> combined:41(purple); evening:28(purple)
- 47 -> combined:25(purple); evening:28(purple)
- 55 -> combined:49(purple); evening:64(purple)
- 77 -> combined:47(purple); evening:112(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.148928571428572)[R1,XVAR-Cons(CEM)], 7(3.85)[R2,XVAR-Cons(CE)], 6(1.1523571428571429)[R1,Mirror-Echo], 0(0.23435714285714285)[R3,Swap], 8(0.23435714285714285)[R3,Swap]
- P2: 3(8.388814285714286)[R1,Mirror-Echo], 8(3.663842857142857)[R2,Mirror-Echo], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0344)[R2,Double-Pressure], 0(0.2881)[R3,Swap]
- P3: 2(8.293657142857143)[R1,XVAR-Cons(CEM)], 0(5.6082)[R2,XVAR-Cons(CEM)], 7(1.4007142857142856)[R1,Mirror-Echo], 4(0.6551999999999999)[R2,Swap], 9(0.1414285714285714)[R3]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Aux snapshot is history-aligned (`excel: data/history/Pick3StatsC4_2025_06_20.xlsm`) and strict alignment passed for this state/day:
    - `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-21 --state Pennsylvania4 --strict` → OK.
- Q2:
  - Positional pressure emphasizes digits 1/3/2 with cross-variant consensus.
  - Winner alignment:
    - 667 (digits 6/6/7): weak positional alignment.
    - 036 (digits 0/3/6): partial alignment (digit 3 is a major consensus digit; digit 0 appears in consensus notes).
- Q3:
  - Positional shortlist top candidates (`132/130/732/...`) do not include either winner directly.
- Q4:
  - Repeat-watch current_index=20; winners indices are 17 and 8 (not in repeat context).
- Q5:
  - VTRAC overlay shows very overdue indices (35/26/4/1/6/...), not winner idx17; winner idx8 is not a highlighted pressure index in Aux.
- Q6:
  - Doubles/pairs:
    - `036` appears explicitly in the Combined overdue doubles list (ds=699), aligning with the Evening winner canonical.
    - Pairs show heavy repeating pressure on 55/77/00/44, which does not align directly with either winner.
- Q7:
  - Sums: the due/flagged sums do not obviously map to either winner as a primary driver.
- Q8:
  - Blackapple is active (score 2; root_due includes 6), but top candidates do not include either winner.
- Q9:
  - Aux convergence (signals counted: `idxTop`, `pair`, `pos`, `BA`, plus “due_double”):

    | candidate | canonical | pos | idxTop | pair | BA | due_double | notes |
    |---|---:|---:|---:|---:|---:|---:|---|
    | 667 | 667 | - | - | ✓ (`66`) | - | - | Midday is mostly Stable-driven |
    | 360 | 036 | - | - | - | - | ✓ (`036` overdue) | best Aux support is “due double” |
    | 013 | 013 | - | - | - | - | - | dominant in winners lens for Evening, not the winner |
    | 168 | 168 | - | - | - | ✓ | - | BA top pick (not winner-aligned) |
- Q10:
  - Aux application recommendation:
    - Use Aux “due doubles” as a candidate-level boost (e.g., elevate 036 if it is already present in tool candidate lists).
    - Avoid using Aux as a day-level gate here because it does not discriminate winner-aligned vs dominant-environment-aligned clusters cleanly.

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
  - `667` (winner canonical) — Stable rank 160/4489, Compound rank 17/1653.
  - `678` — appears in Stable top compound list (and shares digit set).
- Candidate universe (Evening):
  - `036` (winner canonical) — weak tool support but Aux due-double signal exists.
  - `013` / `068` / `018` / `810` — dominant Evening-family survivors (from VTRAC winners stats + Stable compound clusters).
- Evidence vectors:
  - Midday: Stable is the anchor tool for 667.
  - Evening: winners lens indicates 013-family dominance; 036 is not a survivor, but Aux doubles flags it as overdue.
- Coverage mapping + pack decision:
  - Midday: box `667` (6 combos) as the cheapest evidence-respecting pack (would hit Midday winner).
  - Evening: treat as “noisy”; if playing, a small box `036` (6 combos) is justified only because of the due-double flag (would hit Evening winner boxed), but evidence is not otherwise convergent.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday: box `667` covers Midday winner `667` (boxed hit).
  - Evening: box `036` covers Evening winner `360` (boxed hit), but note the environment lens did not elevate 036.
- Key tags:
  - `Stable-midday-strong`, `Evening-013-family-dominance`, `Aux-due-double-036`, `HotZones-low-rank`.
- Drivers:
  - Midday win was driven by Stable’s strong exact + compound evidence for 667.
  - Evening win is better explained as a “due-double hit” (036) inside a dominant 013-family environment.
- Conflicts:
  - Hot Zones is weak on both winners; VTRAC is weak on Midday; Evening winner is not a family survivor even though it hits.
- Fix-now vs fix-later:
  - Fix-now: none (alignment + validators pass).
  - Fix-later: consider explicit logic for “due double canonical” as an overlay that can rescue a low-ranked stable/hz candidate.
- Next run:
  - Contrast Pennsylvania with a state where Evening also has strong Stable/Hot Zones convergence, to avoid building “due doubles” rules off a single example.
