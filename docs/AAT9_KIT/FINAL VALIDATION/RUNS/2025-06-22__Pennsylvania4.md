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
