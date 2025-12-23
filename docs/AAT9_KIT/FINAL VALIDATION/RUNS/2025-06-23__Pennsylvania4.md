# Master Validation Run Report — Pennsylvania4 — results 2025-06-23 (history workbook ~ 2025-06-22)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-23/Pennsylvania4/`
- Winners lens: `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4/`
- Stable: `sharepacks/2025-06-23/Pennsylvania4/stable/Pennsylvania4/`
- Digit Reduction: `sharepacks/2025-06-23/Pennsylvania4/digit_reduction/Pennsylvania4/`
- VTRAC: `sharepacks/2025-06-23/Pennsylvania4/vtrac/Pennsylvania4/`
- Hot Zones: `sharepacks/2025-06-23/Pennsylvania4/hot_zones/Pennsylvania4/`
- Aux: `sharepacks/2025-06-23/Pennsylvania4/aux/Pennsylvania4/`
- Aux draws snapshot: `sharepacks/2025-06-23/Pennsylvania4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac19_winner_164_20251223_052106.html`
- `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac5_winner_040_20251223_052107.html`

Winners JSON files:
- `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac19_winner_164_20251223_052106.json`
- `sharepacks/2025-06-23/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac5_winner_040_20251223_052107.json`

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

### 2.Stable — Pennsylvania4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Pennsylvania4 (2025-06-23)

## Midday winner 164 (canonical 146)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=0 | family_rows=109 | exact_boxed=0 | exact_straight=0 | vt_boxed=0
- Scores (patterns_scores.csv): not present
- Compound (patterns_compound.csv): not present
- Families (patterns_families.csv): 30 rows contain digits; best rank 12, section Combined, score 27.0, hot2 0
- Metrics (metrics.json): exact_boxed=False | exact_straight=False | vt_boxed_count=5
- Coverage gaps: missing_from_scores, missing_from_compound

## Evening winner 040 (canonical 004)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=10 | family_rows=50 | exact_boxed=10 | exact_straight=10 | vt_boxed=10
- Scores (patterns_scores.csv): rank 1034, section Evening, Set Set1, Draw Draw4, Col 3, score 15.0, hot 0, vt_straight 2.0 | why straight|cov1|hp_repeat2|double_mirror|vtrac_straight|set_chain3|draw_chain2
- Compound (patterns_compound.csv): rank 168, section Evening, score 25.0, col1_hits 0, hot2 0, set_chain 3, draw_chain 2 | why set_chain3|draw_chain2|vstrx2|dblmirrorx6
- Families (patterns_families.csv): 23 rows contain digits; best rank 117, section Combined, score 22.5, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=21

## Top compound candidates (patterns_compound.csv)
- rank    3 | canon 138 | section Evening | score 74.0 | col1_hits 7 | hot2 11
- rank    1 | canon 022 | section Midday | score 98.5 | col1_hits 6 | hot2 9
- rank    6 | canon 348 | section Evening | score 60.0 | col1_hits 6 | hot2 8
- rank   14 | canon 1348 | section Evening | score 47.5 | col1_hits 4 | hot2 7
- rank    9 | canon 134 | section Evening | score 52.5 | col1_hits 4 | hot2 7
- rank   12 | canon 389 | section Evening | score 49.0 | col1_hits 4 | hot2 6
- rank   14 | canon 349 | section Evening | score 47.5 | col1_hits 5 | hot2 6
- rank    4 | canon 229 | section Midday | score 70.5 | col1_hits 3 | hot2 6
- rank   19 | canon 3489 | section Evening | score 45.5 | col1_hits 4 | hot2 6
- rank    5 | canon 119 | section Combined | score 65.0 | col1_hits 5 | hot2 6

## Top families (patterns_families.csv)
- rank 1484 | family 14 | score 5.0 | hot2 0 | section Midday
- rank  274 | family 18 | score 19.5 | hot2 0 | section Midday
- rank  489 | family 14 | score 17.0 | hot2 0 | section Midday
- rank  584 | family 23 | score 16.0 | hot2 0 | section Midday
- rank  584 | family 21 | score 16.0 | hot2 0 | section Midday

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

### 2.Digit Reduction — Pennsylvania4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Pennsylvania4 (stamp 20251223)

## Midday winner 164 (canonical 146)
- Stamp (winner_stamp.json): items_total=16 | exact_any=9 exact_final=0 | vtrac_any=16 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=0 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=16 | exact_any=9 vtrac_any=16 | drop_exact_any=0 drop_vtrac_any=0 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=16 vt_straight=0
- Hits (winner_hits.csv): rows=16 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=16 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 040 (canonical 004)
- Stamp (winner_stamp.json): items_total=96 | exact_any=72 exact_final=0 | vtrac_any=84 vtrac_final=0 | drop_exact_any=12 drop_exact_final=0 | drop_vtrac_any=60 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=24 family_vtrac_final=0
- Flags (winner_flags.csv): rows=96 | exact_any=72 vtrac_any=84 | drop_exact_any=12 drop_vtrac_any=60 | family_exact_any=0 family_vtrac_any=24 | vt_boxed=0 vt_straight=0
- Hits (winner_hits.csv): rows=96 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=0 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 164 (canonical 146)
- Stamp (winner_stamp.json): items_total=260 | exact_any=16 exact_final=0 | vtrac_any=258 vtrac_final=0 | drop_exact_any=1 drop_exact_final=0 | drop_vtrac_any=107 drop_vtrac_final=0 | family_exact_any=7 family_exact_final=0 | family_vtrac_any=74 family_vtrac_final=0
- Flags (winner_flags.csv): rows=260 | exact_any=16 vtrac_any=258 | drop_exact_any=1 drop_vtrac_any=107 | family_exact_any=7 family_vtrac_any=74 | vt_boxed=221 vt_straight=0
- Hits (winner_hits.csv): rows=260 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=221 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set3 draw Draw1 col 7 | pattern 224 | score_v2 12.977143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 5 | pattern 220 | score_v2 11.627143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 5 | pattern 220 | score_v2 11.627143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 2 | pattern 922 | score_v2 11.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set3 draw Draw1 col 4 | pattern 220 | score_v2 11.377143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw5 col 1 | pattern 220 | score_v2 11.177143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 994 | score_v2 10.827143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw5 col 1 | pattern 994 | score_v2 10.827143 | match_types 
- area_rank 1 | variant Evening | section Evening | set Set1 draw Draw2 col 4 | pattern 224 | score_v2 10.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw1 col 7 | pattern 992 | score_v2 10.527143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 224 | score_v2 12.977143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Midday | best_pattern 220 | score_v2 11.627143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Midday | best_pattern 922 | score_v2 11.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Evening | best_pattern 994 | score_v2 10.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Midday | best_pattern 992 | score_v2 10.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 224 | score_v2 10.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 922 | score_v2 10.177143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 224 | score_v2 10.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Midday | best_pattern 992 | score_v2 9.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Combined | best_pattern 224 | score_v2 9.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

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

### 2.VTRAC Analyzer — Pennsylvania4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Pennsylvania4 (stamp 20251223_052416)

## Top indices (from enhanced JSON)
- index 28 | score 39.62276 | features: presence=27.36526, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 21 | score 38.3352675 | features: presence=24.367767500000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 8 | score 36.776140000000005 | features: presence=22.528640000000003, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 27 | score 33.11999999999999 | features: presence=19.422499999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 31.180461666666666 | features: presence=18.156294999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 9 | score 30.092587500000004 | features: presence=22.165087500000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 7 | score 27.918600000000005 | features: presence=17.3911, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 30 | score 26.910899999999998 | features: presence=16.7234, cross_section=0.5, set_echo=0.3, first_hit=0.4
- index 11 | score 25.43275 | features: presence=12.61525, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 24 | score 19.699382500000002 | features: presence=13.1218825, cross_section=0.5, set_echo=0.3, first_hit=0.33333333333333337

## Top straights (from enhanced JSON)
018, 019, 208, 201, 871, 817, 091, 687, 810, 081

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 164 | index 19 | file Pennsylvania4_vtrac19_winner_164_20251223_052106.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 040 | index 5 | file Pennsylvania4_vtrac5_winner_040_20251223_052107.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 164 | index 19 rank 30/35 | score 0.6543749999999999 | winner_in_index_straights=False | top_index_straights: (none)
- winner 040 | index 5 rank 29/35 | score 1.790375 | winner_in_index_straights=False | top_index_straights: (none)
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

### 2.Hot Zones — Pennsylvania4 — 2025-06-23

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Pennsylvania4 (2025-06-23)

## Midday winner 164 (canonical 146)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 18
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=False
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 040 (canonical 004)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 184
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 667 | vt_triad 23 | score_mean 21.461 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    2 | triad 226 | vt_triad 23 | score_mean 20.741 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 278 | vt_triad 334 | score_mean 20.545 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    4 | triad 237 | vt_triad 334 | score_mean 20.485 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vertical2,vt_only_lane,vt_straight
- rank    5 | triad 227 | vt_triad 33 | score_mean 19.871 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    5 | triad 277 | vt_triad 33 | score_mean 19.871 | tags funnel_precol1,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,superhot_set1,vertical1,vt_only_lane,vt_straight
- rank    7 | triad 133 | vt_triad 24 | score_mean 19.665 | tags funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 036 | vt_triad 124 | score_mean 19.604 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_straight
- rank    9 | triad 389 | vt_triad 445 | score_mean 19.415 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 229 | vt_triad 35 | score_mean 19.015 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight

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

Aux draws snapshot dir: `sharepacks/2025-06-23/Pennsylvania4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Pennsylvania4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=570, 398, 360, 667, 226
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=398, 667, 354, 041, 954
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=570, 360, 226, 846, 567

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=123 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:3 (gap=43), P3:2 (gap=29)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=876 sev=B
- 012: ds=860 sev=B
- 455: ds=804 sev=B
- 467: ds=734 sev=B
- 059: ds=715 sev=B
- 244: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=53 sev=purple
  - 77: ds=51 sev=purple
  - 00: ds=46 sev=purple
  - 44: ds=45 sev=purple
  - 11: ds=23 sev=-
  - 88: ds=20 sev=-
  - 33: ds=15 sev=-
  - 99: ds=14 sev=-
  - 22: ds=4 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 15: ds=53 sev=blue
  - 23: ds=37 sev=blue
  - 37: ds=34 sev=purple
  - 18: ds=31 sev=purple
  - 47: ds=29 sev=purple
  - 27: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 02: ds=24 sev=-
  - 09: ds=24 sev=-
  - 29: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:257, 26:188, 1:156, 32:151, 4:140, 35:114, 6:86, 5:67, 27:65, 34:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=257 fs=3 fl=2 hz=0.008241758241758242, 26:ds=188 fs=0 fl=1 hz=0.005649717514124294, 1:ds=156 fs=5 fl=3 hz=0.010126582278481013, 32:ds=151 fs=2 fl=1 hz=0.005738880918220947, 4:ds=140 fs=20 fl=1 hz=0.02530120481927711, 35:ds=114 fs=2 fl=0 hz=0.005917159763313609, 6:ds=86 fs=20 fl=0 hz=0.021953896816684963, 5:ds=67 fs=12 fl=2 hz=0.016181229773462785, 27:ds=65 fs=18 fl=3 hz=0.023127753303964757, 34:ds=43 fs=14 fl=4 hz=0.019251336898395723

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=71 flags=purple
- S7: ds=65 flags=purple
- S22: ds=50 flags=purple
- S0: ds=49 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=67 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=13), P2:3 (gap=21), P3:2 (gap=14)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=999 sev=B
- 118: ds=835 sev=B
- 559: ds=784 sev=B
- 018: ds=772 sev=B
- 288: ds=771 sev=B
- 255: ds=742 sev=B
- 668: ds=724 sev=B
- 199: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=26 sev=purple
  - 77: ds=25 sev=purple
  - 00: ds=24 sev=-
  - 22: ds=23 sev=-
  - 44: ds=22 sev=-
  - 88: ds=15 sev=-
  - 11: ds=11 sev=-
  - 99: ds=10 sev=-
  - 33: ds=7 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 48: ds=68 sev=red
  - 25: ds=67 sev=red
  - 68: ds=51 sev=blue
  - 29: ds=50 sev=blue
  - 69: ds=47 sev=blue
  - 28: ds=46 sev=blue
  - 19: ds=45 sev=blue
  - 17: ds=40 sev=blue
  - 03: ds=39 sev=blue
  - 37: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:598, 26:182, 4:175, 1:167, 6:162, 29:134, 16:128, 25:102, 32:75, 12:66

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=598 fs=6 fl=1 hz=0.01881720430107527, 26:ds=182 fs=1 fl=0 hz=0.0028328611898017, 4:ds=175 fs=18 fl=2 hz=0.026075619295958277, 1:ds=167 fs=2 fl=3 hz=0.00904977375565611, 6:ds=162 fs=16 fl=1 hz=0.0228494623655914, 29:ds=134 fs=23 fl=0 hz=0.030666666666666665, 16:ds=128 fs=2 fl=5 hz=0.008728179551122194, 25:ds=102 fs=20 fl=2 hz=0.024608501118568233, 32:ds=75 fs=6 fl=1 hz=0.008781558726673985, 12:ds=66 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=89 flags=red+purple
- S26: ds=81 flags=blue+purple
- S1: ds=80 flags=blue+purple
- S23: ds=76 flags=purple
- S22: ds=63 flags=purple
- S14: ds=37 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 249: score=4 tags=FLT,MIR,RS
  - 267: score=4 tags=FLT,MIR,RS
  - 015: score=3 tags=MIR,RS
  - 024: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 168: score=3 tags=MIR,RS
  - 258: score=3 tags=FLT,RS
  - 348: score=3 tags=MIR,RS
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=39 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=30), P2:5 (gap=41), P3:2 (gap=44)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=41), P3:2 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=910 sev=B
- 788: ds=872 sev=B
- 557: ds=851 sev=B
- 779: ds=845 sev=B
- 278: ds=791 sev=B
- 444: ds=780 sev=B
- 899: ds=777 sev=B
- 778: ds=760 sev=B
- 009: ds=738 sev=B
- 077: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=114 sev=red
  - 55: ds=66 sev=purple
  - 33: ds=44 sev=purple
  - 66: ds=32 sev=purple
  - 44: ds=30 sev=purple
  - 00: ds=23 sev=-
  - 11: ds=16 sev=-
  - 88: ds=10 sev=-
  - 99: ds=7 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 59: ds=66 sev=red
  - 49: ds=57 sev=red
  - 78: ds=50 sev=blue
  - 23: ds=38 sev=blue
  - 39: ds=35 sev=purple
  - 15: ds=34 sev=purple
  - 89: ds=33 sev=purple
  - 47: ds=30 sev=purple
  - 12: ds=29 sev=purple
  - 04: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:424, 16:211, 28:151, 26:94, 15:82, 1:78, 17:73, 4:70, 5:66, 30:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=424 fs=0 fl=1 hz=0.004405286343612335, 16:ds=211 fs=4 fl=4 hz=0.011142061281337047, 28:ds=151 fs=14 fl=3 hz=0.020118343195266272, 26:ds=94 fs=2 fl=0 hz=0.005242463958060288, 15:ds=82 fs=35 fl=0 hz=0.042682926829268296, 1:ds=78 fs=8 fl=3 hz=0.013480392156862744, 17:ds=73 fs=24 fl=1 hz=0.02824858757062147, 4:ds=70 fs=28 fl=1 hz=0.03125, 5:ds=66 fs=15 fl=4 hz=0.020496224379719524, 30:ds=64 fs=39 fl=0 hz=0.04314159292035399

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=60 flags=purple
- S7: ds=54 flags=purple
- S8: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:715(B); evening:717(B)
- 255 -> evening:696(B); midday:742(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 15 -> combined:53(blue); evening:34(purple); midday:26(purple)
- 23 -> combined:37(blue); evening:38(blue)
- 37 -> combined:34(purple); midday:31(purple)
- 44 -> combined:45(purple); evening:30(purple)
- 47 -> combined:29(purple); evening:30(purple)
- 55 -> combined:53(purple); evening:66(purple); midday:26(purple)
- 77 -> combined:51(purple); evening:114(red); midday:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.271114285714286)[R1,XVAR-Cons(CEM)], 7(3.9977142857142858)[R2,XVAR-Cons(CE)], 8(0.9508)[R2,Double-Pressure], 0(0.2612285714285714)[R3,Swap], 4(0.18385714285714286)[R3]
- P2: 3(8.702542857142857)[R1,Mirror-Echo], 8(3.797714285714286)[R2,Mirror-Echo], 0(1.8846857142857143)[R3,XVAR-Cons(CM)], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0761999999999998)[R2,Double-Pressure]
- P3: 2(8.274428571428572)[R1,XVAR-Cons(CEM)], 9(2.342357142857143)[R2,XVAR-Cons(CM)], 3(1.9391357142857144)[R3,XVAR-Cons(CE)], 4(1.2269999999999999)[R2,Double-Pressure], 0(0.9508)[R2,Double-Pressure]

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
