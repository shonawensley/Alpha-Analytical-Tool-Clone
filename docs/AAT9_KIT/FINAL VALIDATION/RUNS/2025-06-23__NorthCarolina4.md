# Master Validation Run Report — NorthCarolina4 — results 2025-06-23 (history workbook ~ 2025-06-22)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-23/NorthCarolina4/`
- Winners lens: `sharepacks/2025-06-23/NorthCarolina4/winners/NorthCarolina4/`
- Stable: `sharepacks/2025-06-23/NorthCarolina4/stable/NorthCarolina4/`
- Digit Reduction: `sharepacks/2025-06-23/NorthCarolina4/digit_reduction/NorthCarolina4/`
- VTRAC: `sharepacks/2025-06-23/NorthCarolina4/vtrac/NorthCarolina4/`
- Hot Zones: `sharepacks/2025-06-23/NorthCarolina4/hot_zones/NorthCarolina4/`
- Aux: `sharepacks/2025-06-23/NorthCarolina4/aux/NorthCarolina4/`
- Aux draws snapshot: `sharepacks/2025-06-23/NorthCarolina4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-23/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac12_winner_920_20251223_052057.html`
- `sharepacks/2025-06-23/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac9_winner_145_20251223_052059.html`

Winners JSON files:
- `sharepacks/2025-06-23/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac12_winner_920_20251223_052057.json`
- `sharepacks/2025-06-23/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac9_winner_145_20251223_052059.json`

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

### 2.Stable — NorthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — NorthCarolina4 (2025-06-23)

## Midday winner 920 (canonical 029)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=407 | exact_boxed=10 | exact_straight=8 | vt_boxed=10
- Scores (patterns_scores.csv): rank 3993, section Midday, Set Set1, Draw Draw6, Col 1, score 12.0, hot 1, vt_straight 2.0 | why straight|cov1|hot1|vtrac_straight|draw_chain3
- Compound (patterns_compound.csv): rank 500, section Midday, score 19.0, col1_hits 1, hot2 0, set_chain 1, draw_chain 5 | why draw_chain5|col1x1|hot1x2|vstrx3
- Families (patterns_families.csv): 82 rows contain digits; best rank 43, section Midday, score 26.5, hot2 5
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=72

## Evening winner 145 (canonical 145)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=17 | family_rows=280 | exact_boxed=17 | exact_straight=13 | vt_boxed=17
- Scores (patterns_scores.csv): rank 87, section Evening, Set Set3, Draw Draw1, Col 1, score 24.0, hot 1, vt_straight 0.0 | why boxed|cov4|hp_repeat2|vstr2|hot1|dom_last|perm3|set_chain3
- Compound (patterns_compound.csv): rank 23, section Evening, score 50.0, col1_hits 2, hot2 4, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x2|hot1x7|hot2x4|vstrx7
- Families (patterns_families.csv): 57 rows contain digits; best rank 26, section Evening, score 27.5, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=107

## Top compound candidates (patterns_compound.csv)
- rank   10 | canon 456 | section Evening | score 58.0 | col1_hits 3 | hot2 7
- rank   12 | canon 1388 | section Combined | score 56.0 | col1_hits 1 | hot2 6
- rank    8 | canon 348 | section Combined | score 58.5 | col1_hits 2 | hot2 6
- rank   16 | canon 1348 | section Combined | score 53.0 | col1_hits 2 | hot2 6
- rank   16 | canon 3488 | section Combined | score 53.0 | col1_hits 1 | hot2 6
- rank   15 | canon 3348 | section Midday | score 54.0 | col1_hits 5 | hot2 6
- rank    5 | canon 134 | section Combined | score 60.5 | col1_hits 2 | hot2 6
- rank   14 | canon 338 | section Midday | score 54.5 | col1_hits 5 | hot2 6
- rank    3 | canon 455 | section Evening | score 65.5 | col1_hits 1 | hot2 6
- rank    6 | canon 138 | section Combined | score 59.5 | col1_hits 2 | hot2 6

## Top families (patterns_families.csv)
- rank 1243 | family 27 | score 9.0 | hot2 0 | section Midday
- rank 1140 | family 21 | score 10.5 | hot2 0 | section Midday
- rank  181 | family 23 | score 22.5 | hot2 0 | section Midday
- rank  315 | family 32 | score 20.5 | hot2 0 | section Midday
- rank  413 | family 31 | score 19.0 | hot2 0 | section Midday

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

### 2.Digit Reduction — NorthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — NorthCarolina4 (stamp 20251223)

## Midday winner 920 (canonical 029)
- Stamp (winner_stamp.json): items_total=252 | exact_any=0 exact_final=0 | vtrac_any=216 vtrac_final=0 | drop_exact_any=26 drop_exact_final=0 | drop_vtrac_any=228 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=72 family_vtrac_final=0
- Flags (winner_flags.csv): rows=252 | exact_any=0 vtrac_any=216 | drop_exact_any=26 drop_vtrac_any=228 | family_exact_any=0 family_vtrac_any=72 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=252 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 145 (canonical 145)
- Stamp (winner_stamp.json): items_total=112 | exact_any=60 exact_final=0 | vtrac_any=97 vtrac_final=0 | drop_exact_any=71 drop_exact_final=0 | drop_vtrac_any=75 drop_vtrac_final=0 | family_exact_any=12 family_exact_final=0 | family_vtrac_any=9 family_vtrac_final=0
- Flags (winner_flags.csv): rows=112 | exact_any=60 vtrac_any=97 | drop_exact_any=71 drop_vtrac_any=75 | family_exact_any=12 family_vtrac_any=9 | vt_boxed=24 vt_straight=0
- Hits (winner_hits.csv): rows=112 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=24 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 920 (canonical 029)
- Stamp (winner_stamp.json): items_total=478 | exact_any=0 exact_final=0 | vtrac_any=365 vtrac_final=0 | drop_exact_any=46 drop_exact_final=0 | drop_vtrac_any=454 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=159 family_vtrac_final=0
- Flags (winner_flags.csv): rows=478 | exact_any=0 vtrac_any=365 | drop_exact_any=46 drop_vtrac_any=454 | family_exact_any=0 family_vtrac_any=159 | vt_boxed=34 vt_straight=0
- Hits (winner_hits.csv): rows=478 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=34 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → None | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 244 | score_v2 13.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 7 | pattern 244 | score_v2 11.558571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set2 draw Draw1 col 6 | pattern 440 | score_v2 11.04381 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 6 | pattern 224 | score_v2 10.99381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 940 | score_v2 10.877143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 5 | pattern 224 | score_v2 10.74381 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 5 | pattern 224 | score_v2 10.74381 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 6 | pattern 244 | score_v2 10.627143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 924 | score_v2 10.128571 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 2 | pattern 554 | score_v2 9.627143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 244 | score_v2 13.027143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 440 | score_v2 11.04381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 224 | score_v2 10.99381 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 940 | score_v2 10.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 244 | score_v2 10.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Combined | best_pattern 924 | score_v2 10.128571 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Evening | best_pattern 554 | score_v2 9.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Combined | best_pattern 922 | score_v2 9.620476 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 240 | score_v2 9.597143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 524 | score_v2 9.587143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

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

### 2.VTRAC Analyzer — NorthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — NorthCarolina4 (stamp 20251223_052414)

## Top indices (from enhanced JSON)
- index 23 | score 95.59938749999996 | features: presence=70.35188749999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 24 | score 59.41518999999999 | features: presence=39.71768999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 32 | score 54.41219499999999 | features: presence=40.67469499999999, set_echo=0.6, first_hit=0.4, column_span=0.3375
- index 19 | score 47.730155 | features: presence=31.712655, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 9 | score 41.8883625 | features: presence=28.5508625, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 22 | score 35.014900000000004 | features: presence=19.637400000000007, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 34.34760000000001 | features: presence=24.370100000000004, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 28.95507999999999 | features: presence=20.19757999999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 28.518199999999997 | features: presence=19.9407, set_echo=0.3, first_hit=0.4, column_span=0.3375
- index 16 | score 24.498875 | features: presence=16.013250000000003, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
138, 813, 386, 683, 836, 183, 413, 541, 341, 624

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 920 | index 12 | file NorthCarolina4_vtrac12_winner_920_20251223_052057.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 145 | index 9 | file NorthCarolina4_vtrac9_winner_145_20251223_052059.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 920 | index 12 rank 18/35 | score 12.52555 | winner_in_index_straights=False | top_index_straights: 524 (6.858), 245 (6.204), 259 (3.836)
- winner 145 | index 9 rank 5/35 | score 41.8883625 | winner_in_index_straights=True | top_index_straights: 541 (17.745), 645 (13.245), 564 (12.733)
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

### 2.Hot Zones — NorthCarolina4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — NorthCarolina4 (2025-06-23)

## Midday winner 920 (canonical 029)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 20
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 145 (canonical 145)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 69
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 247 | vt_triad 335 | score_mean 24.253 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    2 | triad 379 | vt_triad 345 | score_mean 24.164 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical5,vt_only_lane,vt_straight
- rank    3 | triad 567 | vt_triad 123 | score_mean 23.161 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 077 | vt_triad 13 | score_mean 22.981 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_straight
- rank    5 | triad 229 | vt_triad 35 | score_mean 21.85 | tags hot16,hot20,set1_bonus,straight_lane,vertical1,vertical2,vt_only_lane,vt_straight
- rank    6 | triad 224 | vt_triad 35 | score_mean 21.362 | tags hot12,hot16,hot20,ls_col_42,set1_bonus,straight_lane,vertical1,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 126 | vt_triad 223 | score_mean 21.335 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 228 | vt_triad 34 | score_mean 21.25 | tags hot20,set1_bonus
- rank    8 | triad 377 | vt_triad 34 | score_mean 21.25 | tags hot20,set1_bonus
- rank   10 | triad 257 | vt_triad 133 | score_mean 20.917 | tags funnel_precol1,hot12,hot16,hot20,literal_draw,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight

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

Aux draws snapshot dir: `sharepacks/2025-06-23/NorthCarolina4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — NorthCarolina4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=153, 765, 397, 427, 261
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=765, 427, 707, 579, 257
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=153, 397, 261, 902, 799

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=7 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=16), P2:4 (gap=17), P3:4 (gap=33)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=831 sev=B
- 228: ds=824 sev=B
- 244: ds=798 sev=B
- 004: ds=772 sev=B
- 001: ds=736 sev=B
- 677: ds=697 sev=B
- 377: ds=695 sev=B
- 044: ds=693 sev=B
- 226: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=103 sev=blue
  - 44: ds=57 sev=purple
  - 66: ds=50 sev=purple
  - 11: ds=40 sev=purple
  - 33: ds=38 sev=purple
  - 22: ds=29 sev=purple
  - 55: ds=28 sev=purple
  - 00: ds=10 sev=-
  - 99: ds=8 sev=-
  - 77: ds=5 sev=-
- non_repeating:
  - 89: ds=132 sev=red
  - 46: ds=100 sev=red
  - 36: ds=38 sev=blue
  - 49: ds=35 sev=purple
  - 14: ds=33 sev=purple
  - 23: ds=32 sev=purple
  - 06: ds=26 sev=purple
  - 01: ds=23 sev=-
  - 28: ds=18 sev=-
  - 68: ds=18 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:377, 16:245, 35:201, 29:153, 15:107, 26:94, 2:78, 6:77, 27:61, 25:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=377 fs=0 fl=2 hz=0.0049504950495049506, 16:ds=245 fs=0 fl=1 hz=0.0036900369003690036, 35:ds=201 fs=0 fl=2 hz=0.005154639175257732, 29:ds=153 fs=19 fl=1 hz=0.02442002442002442, 15:ds=107 fs=21 fl=0 hz=0.025059665871121718, 26:ds=94 fs=3 fl=1 hz=0.007109004739336493, 2:ds=78 fs=22 fl=0 hz=0.024017467248908297, 6:ds=77 fs=23 fl=3 hz=0.029213483146067414, 27:ds=61 fs=12 fl=1 hz=0.016587677725118485, 25:ds=57 fs=17 fl=4 hz=0.022364217252396165

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=86 flags=purple
- S2: ds=84 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 2}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=16 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=20), P2:3 (gap=21), P3:3 (gap=64)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:3 (ds=64)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 344: ds=830 sev=B
- 188: ds=823 sev=B
- 558: ds=780 sev=B
- 115: ds=772 sev=B
- 123: ds=755 sev=B
- 446: ds=732 sev=B
- 335: ds=696 sev=B
- 777: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=89 sev=blue
  - 33: ds=64 sev=purple
  - 88: ds=51 sev=purple
  - 00: ds=48 sev=purple
  - 55: ds=41 sev=purple
  - 66: ds=36 sev=purple
  - 44: ds=28 sev=purple
  - 22: ds=14 sev=-
  - 99: ds=9 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 89: ds=78 sev=red
  - 46: ds=75 sev=red
  - 28: ds=66 sev=red
  - 26: ds=50 sev=blue
  - 29: ds=42 sev=blue
  - 15: ds=38 sev=blue
  - 36: ds=36 sev=purple
  - 03: ds=32 sev=purple
  - 23: ds=30 sev=purple
  - 37: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:188, 26:185, 1:180, 16:122, 35:100, 33:80, 22:79, 29:76, 20:72, 23:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=188 fs=3 fl=2 hz=0.007741935483870969, 26:ds=185 fs=1 fl=0 hz=0.0049382716049382715, 1:ds=180 fs=3 fl=3 hz=0.00857843137254902, 16:ds=122 fs=2 fl=1 hz=0.009174311926605505, 35:ds=100 fs=0 fl=1 hz=0.00487012987012987, 33:ds=80 fs=21 fl=2 hz=0.026744186046511628, 22:ds=79 fs=44 fl=0 hz=0.04851157662624035, 29:ds=76 fs=17 fl=2 hz=0.02132435465768799, 20:ds=72 fs=22 fl=1 hz=0.02481121898597627, 23:ds=70 fs=17 fl=2 hz=0.021300448430493273

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
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '8'], 'pairs': {'remaining_count': 0}}
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
  - 028: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=23 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=32), P3:4 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=986 sev=B
- 668: ds=970 sev=B
- 166: ds=865 sev=B
- 378: ds=864 sev=B
- 666: ds=862 sev=B
- 455: ds=856 sev=B
- 225: ds=826 sev=B
- 279: ds=817 sev=B
- 111: ds=781 sev=B
- 222: ds=780 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=65 sev=purple
  - 88: ds=58 sev=purple
  - 22: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 11: ds=20 sev=-
  - 33: ds=19 sev=-
  - 55: ds=14 sev=-
  - 77: ds=7 sev=-
  - 00: ds=5 sev=-
  - 99: ds=4 sev=-
- non_repeating:
  - 04: ds=103 sev=red
  - 89: ds=66 sev=red
  - 45: ds=50 sev=blue
  - 46: ds=50 sev=blue
  - 01: ds=42 sev=blue
  - 69: ds=36 sev=purple
  - 59: ds=35 sev=purple
  - 49: ds=32 sev=purple
  - 57: ds=24 sev=-
  - 18: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:634, 35:300, 32:251, 5:126, 14:106, 29:79, 15:68, 34:65, 27:49, 9:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=634 fs=4 fl=1 hz=0.0154320987654321, 35:ds=300 fs=1 fl=3 hz=0.008032128514056224, 32:ds=251 fs=3 fl=2 hz=0.00946372239747634, 5:ds=126 fs=18 fl=1 hz=0.02328288707799767, 14:ds=106 fs=39 fl=0 hz=0.04426787741203178, 29:ds=79 fs=18 fl=2 hz=0.023781212841854936, 15:ds=68 fs=15 fl=2 hz=0.019653179190751446, 34:ds=65 fs=19 fl=0 hz=0.023086269744835963, 27:ds=49 fs=19 fl=4 hz=0.02454642475987193, 9:ds=48 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=75 flags=purple
- S23: ds=68 flags=purple
- S20: ds=58 flags=purple
- S0: ds=57 flags=blue+purple
- S10: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 666 -> combined:831(B); evening:862(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:26(purple); midday:25(purple)
- 11 -> combined:40(purple); midday:89(blue)
- 22 -> combined:29(purple); evening:26(purple)
- 23 -> combined:32(purple); midday:30(purple)
- 33 -> combined:38(purple); midday:64(purple)
- 36 -> combined:38(blue); midday:36(purple)
- 44 -> combined:57(purple); evening:65(purple); midday:28(purple)
- 46 -> combined:100(red); evening:50(blue); midday:75(red)
- 49 -> combined:35(purple); evening:32(purple)
- 55 -> combined:28(purple); midday:41(purple)
- 66 -> combined:50(purple); evening:25(purple); midday:36(purple)
- 88 -> combined:103(blue); evening:58(purple); midday:51(purple)
- 89 -> combined:132(red); evening:66(red); midday:78(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(3.0859)[R2,XVAR-Cons(CE)], 8(2.8385714285714285)[R3,XVAR-Cons(CM)], 0(2.700342857142857)[R1,XVAR-Cons(CE)], 5(1.066857142857143)[R1,Mirror-Echo], 1(1.0344)[R2,Double-Pressure]
- P2: 4(7.656914285714286)[R1,XVAR-Cons(CEM)], 3(3.0594642857142857)[R3,Mirror-Echo], 8(2.8861928571428574)[R2,Mirror-Echo], 1(1.1179999999999999)[R2,Double-Pressure], 2(0.21497142857142856)[R3]
- P3: 4(7.968685714285715)[R1,XVAR-Cons(CEM)], 6(6.415035714285714)[R2,XVAR-Cons(CEM)], 3(1.7449999999999999)[R1,Double-Pressure], 8(0.25557142857142856)[R3,Swap], 5(0.13435714285714284)[R3]

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
