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
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …
- Q11: …
- Q12: …
- Q13: …
- Q14: …

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
# Stable Summary — 2025-06-21

## Midday winner 667 (canonical 667)
- Spotlight (winner_family_spotlight_raw.csv): 12 rows | exact_boxed=12 | exact_straight=12 | vt_boxed=12
- Scores (patterns_scores.csv): rank 160, section Midday, Set Set1, Draw Draw4, Col 1, score 21.5, hot 2, vt_straight 2.0 | why straight|cov1|hp_repeat4|hot2|hidden3v|double_mirror|vtrac_straight|set_chain2|draw_chain4
- Compound (patterns_compound.csv): rank 17, section Midday, score 48.5, col1_hits 4, hot2 4, set_chain 2, draw_chain 4 | why set_chain2|draw_chain4|col1x4|hot1x1|hot2x4|vstrx9|dblmirrorx11
- Families (patterns_families.csv): 67 rows contain digits; best rank 18, section Combined, score 27.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=11

## Evening winner 360 (canonical 036)
- Spotlight (winner_family_spotlight_raw.csv): 0 rows | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 24 rows contain digits; best rank 516, section Midday, score 16.5, hot2 2
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=81
- Coverage gaps: missing_from_spotlight, missing_from_scores, missing_from_compound

## Top compound candidates (patterns_compound.csv)
- rank    5 | canon 38 | section Evening | score 63.0 | col1_hits 6 | hot2 8
- rank    4 | canon 229 | section Midday | score 68.0 | col1_hits 6 | hot2 8
- rank    8 | canon 228 | section Midday | score 60.5 | col1_hits 3 | hot2 7
- rank    9 | canon 338 | section Evening | score 56.5 | col1_hits 5 | hot2 6
- rank   11 | canon 133 | section Evening | score 54.0 | col1_hits 5 | hot2 6
- rank   12 | canon 1338 | section Evening | score 51.5 | col1_hits 4 | hot2 6
- rank   14 | canon 1338 | section Evening | score 49.5 | col1_hits 5 | hot2 6
- rank   17 | canon 678 | section Midday | score 48.5 | col1_hits 3 | hot2 6
- rank   30 | canon 338 | section Evening | score 44.5 | col1_hits 5 | hot2 6
- rank   33 | canon 13 | section Evening | score 43.5 | col1_hits 4 | hot2 6

## Top families (patterns_families.csv)
- rank 1364 | family 2 | score 3.0 | hot2 0 | section Midday
- rank 1360 | family 19 | score 4.0 | hot2 0 | section Midday
- rank  126 | family 28 | score 22.0 | hot2 3 | section Midday
- rank  676 | family 20 | score 14.5 | hot2 1 | section Midday
- rank  885 | family 24 | score 12.5 | hot2 1 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …

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
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 360 (canonical 036)
- Stamp (winner_stamp.json): items_total=204 | exact_any=0 exact_final=0 | vtrac_any=202 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=51 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=15 family_vtrac_final=0
- Flags (winner_flags.csv): rows=204 | exact_any=0 vtrac_any=202 | drop_exact_any=0 drop_vtrac_any=51 | family_exact_any=0 family_vtrac_any=15 | vt_boxed=36 vt_straight=0
- Hits (winner_hits.csv): rows=204 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=36 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 667 (canonical 667)
- Stamp (winner_stamp.json): items_total=236 | exact_any=132 exact_final=0 | vtrac_any=236 vtrac_final=0 | drop_exact_any=6 drop_exact_final=0 | drop_vtrac_any=122 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=236 | exact_any=132 vtrac_any=236 | drop_exact_any=6 drop_vtrac_any=122 | family_exact_any=0 family_vtrac_any=9 | vt_boxed=139 vt_straight=0
- Hits (winner_hits.csv): rows=236 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=139 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 990 | score_v2 11.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 599 | score_v2 10.958571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw1 col 2 | pattern 3 | score_v2 10.864643 | match_types 
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
- rank 3 | variant Evening | best_pattern 3 | score_v2 10.864643 | tags exact,vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 922 | score_v2 10.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 599 | score_v2 10.308571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 599 | score_v2 10.208571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 599 | score_v2 10.158571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 228 | score_v2 10.064643 | tags exact,vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 922 | score_v2 9.737143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 992 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …

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
- winner 667 | index 17 | file Pennsylvania4_vtrac17_winner_667_20251219_164416.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 360 | index 8 | file Pennsylvania4_vtrac8_winner_360_20251219_164417.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 667 | index 17 rank 16/35 | score 6.165958333333333 | winner_in_index_straights=False | top_index_straights: 617 (1.266), 167 (1.245), 162 (0.69)
- winner 360 | index 8 rank 7/35 | score 22.624785000000003 | winner_in_index_straights=False | top_index_straights: 018 (9.652), 013 (7.457), 810 (6.481)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …

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
- Top lanes (hot_zones_top_lanes.csv): present, best rank 157
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 360 (canonical 036)
- Top lanes (hot_zones_top_lanes.csv): not present
- Per-lane (hot_zones_per_lane.csv): not present
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: missing_from_top_lanes, missing_from_per_lane, winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 277 | vt_triad 33 | score_mean 22.783 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    1 | triad 227 | vt_triad 33 | score_mean 22.783 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    3 | triad 459 | vt_triad 155 | score_mean 22.718 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    4 | triad 0 | vt_triad 1 | score_mean 22.0 | tags col1,funnel_precol1,hot16,ls_col_42,straight_lane,vertical4
- rank    5 | triad 11 | vt_triad 12 | score_mean 20.667 | tags hot12,hot16,hot20,set1_bonus,straight_lane,vertical2,vertical3,vt_straight
- rank    6 | triad 3 | vt_triad 14 | score_mean 20.633 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical4,vt_only_lane,vt_straight
- rank    7 | triad 56 | vt_triad 112 | score_mean 20.347 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical5,vt_only_lane,vt_straight
- rank    8 | triad 267 | vt_triad 233 | score_mean 20.167 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    8 | triad 127 | vt_triad 233 | score_mean 20.167 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank   10 | triad 466 | vt_triad 25 | score_mean 19.8 | tags hot16,hot8,literal_draw,set1_bonus,straight_lane,vertical1,vertical3,vertical5,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals: …
- Conflicts/noise: …
- Aggregator/aux hooks to test next: …

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
- Q1: …
- Q2: …
- Q3: …
- Q4: …
- Q5: …
- Q6: …
- Q7: …
- Q8: …
- Q9: …
- Q10: …

---

## Part 4 — Combination / Permutation Translation (candidate pack)
Use Part 4 prompts in the master template to produce:
- A small candidate universe per draw (Midday/Evening)
- Evidence vectors per candidate (tools + aux signals)
- Coverage mapping (perm-only vs boxed vs VTRAC-straight vs full index-box)

Reference:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

Part 4 notes / answers:
- Candidate universe (Midday): …
- Candidate universe (Evening): …
- Evidence vectors: …
- Coverage mapping + pack decision: …

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners: …
- Key tags: …
- Drivers: …
- Conflicts: …
- Fix-now vs fix-later: …
- Next run: …
