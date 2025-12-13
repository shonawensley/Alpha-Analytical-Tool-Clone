# Master Validation Run Report — OntarioCanada4 — results 2025-06-21 (history workbook ~ 2025-06-20)

Reference template:
- `tasks/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-21/OntarioCanada4/`
- Winners lens: `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-06-21/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-06-21/OntarioCanada4/hot_zones/OntarioCanada4/`
- Aux: `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/`
- Aux draws snapshot: `sharepacks/2025-06-21/OntarioCanada4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251201_233402.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_081811.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_133329.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_134134.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251209_181934.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251201_233403.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_081812.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_133331.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_134135.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251209_181936.html`

Winners JSON files:
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_081811.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_133329.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251206_134134.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251209_181934.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_081812.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_133331.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251206_134135.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251209_181936.json`

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

### 2.Stable — OntarioCanada4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — 2025-06-21

## Midday winner 678 (canonical 678)
- Spotlight (winner_family_spotlight_raw.csv): 14 rows | exact_boxed=14 | exact_straight=7 | vt_boxed=14
- Scores (patterns_scores.csv): rank 365, section Midday, Set Set3, Draw Draw1, Col 4, score 21.0, hot 1, vt_straight 0.0 | why boxed|cov4|hp_repeat3|vstr2|hot1|perm3|set_chain3
- Compound (patterns_compound.csv): rank 141, section Midday, score 29.0, col1_hits 1, hot2 0, set_chain 3, draw_chain 3 | why set_chain3|draw_chain3|col1x1|hot1x1|vstrx1
- Families (patterns_families.csv): 37 rows contain digits; best rank 262, section Midday, score 21.0, hot2 1
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=93

## Evening winner 517 (canonical 157)
- Spotlight (winner_family_spotlight_raw.csv): 13 rows | exact_boxed=9 | exact_straight=9 | vt_boxed=13
- Scores (patterns_scores.csv): rank 3100, section Combined, Set Set3, Draw Draw1, Col 7, score 12.0, hot 0, vt_straight 0.0 | why straight|cov1|hp_repeat3|set_chain3
- Compound (patterns_compound.csv): rank 598, section Combined, score 16.5, col1_hits 0, hot2 0, set_chain 3, draw_chain 1 | why set_chain3|draw_chain1
- Families (patterns_families.csv): 50 rows contain digits; best rank 200, section Midday, score 22.0, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=50

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 229 | section Evening | score 92.5 | col1_hits 7 | hot2 11
- rank    3 | canon 225 | section Evening | score 77.5 | col1_hits 6 | hot2 8
- rank    2 | canon 9 | section Combined | score 80.0 | col1_hits 7 | hot2 8
- rank    5 | canon 259 | section Evening | score 70.0 | col1_hits 6 | hot2 8
- rank    8 | canon 2259 | section Evening | score 63.5 | col1_hits 6 | hot2 8
- rank    4 | canon 224 | section Evening | score 76.0 | col1_hits 3 | hot2 7
- rank    6 | canon 2249 | section Evening | score 66.0 | col1_hits 3 | hot2 7
- rank   10 | canon 239 | section Evening | score 59.5 | col1_hits 1 | hot2 6
- rank   29 | canon 59 | section Combined | score 47.5 | col1_hits 3 | hot2 6
- rank   21 | canon 22349 | section Evening | score 51.0 | col1_hits 0 | hot2 6

## Top families (patterns_families.csv)
- rank 1229 | family 6 | score 7.5 | hot2 0 | section Midday
- rank  910 | family 30 | score 12.0 | hot2 2 | section Midday
- rank 1188 | family 15 | score 8.5 | hot2 0 | section Midday
- rank 1229 | family 3 | score 7.5 | hot2 0 | section Midday
- rank 1275 | family 7 | score 6.0 | hot2 0 | section Midday

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

### 2.Digit Reduction — OntarioCanada4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — OntarioCanada4 (stamp 20251209)

## Midday winner 678 (canonical 678)
- Stamp (winner_stamp.json): items_total=112 | exact_any=108 exact_final=0 | vtrac_any=112 vtrac_final=0 | drop_exact_any=5 drop_exact_final=0 | drop_vtrac_any=15 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=112 | exact_any=108 vtrac_any=112 | drop_exact_any=5 drop_vtrac_any=15 | family_exact_any=2 family_vtrac_any=2 | vt_boxed=9 vt_straight=0
- Hits (winner_hits.csv): rows=112 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=9 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Evening winner 517 (canonical 157)
- Stamp (winner_stamp.json): items_total=112 | exact_any=0 exact_final=0 | vtrac_any=102 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=32 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=14 family_vtrac_final=0
- Flags (winner_flags.csv): rows=112 | exact_any=0 vtrac_any=102 | drop_exact_any=0 drop_vtrac_any=32 | family_exact_any=0 family_vtrac_any=14 | vt_boxed=112 vt_straight=0
- Hits (winner_hits.csv): rows=112 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=112 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Combined winner 678 (canonical 678)
- Stamp (winner_stamp.json): items_total=250 | exact_any=156 exact_final=0 | vtrac_any=250 vtrac_final=0 | drop_exact_any=5 drop_exact_final=0 | drop_vtrac_any=15 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=2 family_vtrac_final=0
- Flags (winner_flags.csv): rows=250 | exact_any=156 vtrac_any=250 | drop_exact_any=5 drop_vtrac_any=15 | family_exact_any=2 family_vtrac_any=2 | vt_boxed=15 vt_straight=0
- Hits (winner_hits.csv): rows=250 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=15 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): winner_triads_as_candidates=False | winner_best_rank=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 16.287143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 1 | pattern 599 | score_v2 15.787143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 599 | score_v2 15.777143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 599 | score_v2 15.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 599 | score_v2 15.027143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 599 | score_v2 14.937143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 599 | score_v2 14.927143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw7 col 1 | pattern 559 | score_v2 14.827143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 14.827143 | match_types 
- area_rank 2 | variant Combined | section Combined | set Set1 draw Draw6 col 1 | pattern 559 | score_v2 14.537143 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 16.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 14.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 599 | score_v2 13.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 599 | score_v2 12.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 592 | score_v2 11.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Midday | best_pattern 559 | score_v2 11.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Combined | best_pattern 559 | score_v2 11.837143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Evening | best_pattern 559 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 592 | score_v2 11.727143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Midday | best_pattern 599 | score_v2 11.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

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

### 2.VTRAC Analyzer — OntarioCanada4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — OntarioCanada4 (stamp 20251209_193731)

## Top indices (from enhanced JSON)
- index 20 | score 49.543432499999994 | features: presence=29.6859325, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 23 | score 42.80004499999999 | features: presence=27.332544999999996, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 30 | score 30.6818 | features: presence=18.074299999999997, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 27 | score 25.694610000000004 | features: presence=16.22711, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 28 | score 23.195875000000004 | features: presence=16.518375000000002, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 10 | score 20.543130000000005 | features: presence=11.975630000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 29 | score 20.207360000000005 | features: presence=12.15986, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 24 | score 20.0703875 | features: presence=12.3528875, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 33 | score 17.751500000000004 | features: presence=11.214000000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667
- index 18 | score 16.9982925 | features: presence=8.1807925, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
932, 923, 293, 259, 193, 592, 593, 362, 963, 913

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 678 | index 21 | file OntarioCanada4_vtrac21_winner_678_20251209_181934.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 517 | index 7 | file OntarioCanada4_vtrac7_winner_517_20251209_181936.json | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 678 | index 21 rank 14/35 | score 11.84887 | winner_in_index_straights=False | top_index_straights: 362 (5.836), 213 (3.879), 263 (2.859)
- winner 517 | index 7 rank 21/35 | score 8.263768333333333 | winner_in_index_straights=False | top_index_straights: 256 (2.408), 625 (1.976), 201 (1.888)
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

### 2.Hot Zones — OntarioCanada4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — OntarioCanada4 (2025-06-21)

## Midday winner 678 (canonical 678)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 92
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Evening winner 517 (canonical 157)
- Top lanes (hot_zones_top_lanes.csv): present, best rank 106
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False
- Coverage gaps: winner_not_in_winner_map

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 227 | vt_triad 33 | score_mean 23.308 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    2 | triad 277 | vt_triad 33 | score_mean 23.238 | tags col1,funnel_precol1,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    3 | triad 267 | vt_triad 233 | score_mean 21.683 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    4 | triad 127 | vt_triad 233 | score_mean 21.3 | tags col1,funnel_precol1,hot12,hot16,hot20,ls2_lane,ls_col_42,set1_bonus,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 578 | vt_triad 134 | score_mean 21.278 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vt_only_lane,vt_straight
- rank    6 | triad 334 | vt_triad 45 | score_mean 20.738 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vertical5,vt_only_lane,vt_straight
- rank    7 | triad 146 | vt_triad 225 | score_mean 20.604 | tags funnel_precol1,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 226 | vt_triad 23 | score_mean 20.093 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    9 | triad 367 | vt_triad 234 | score_mean 20.075 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank   10 | triad 122 | vt_triad 23 | score_mean 19.916 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

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

Aux draws snapshot dir: `sharepacks/2025-06-21/OntarioCanada4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — OntarioCanada4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/OntarioCanada4/aux/draws`
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=790, 242, 644, 072, 630
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=242, 072, 595, 010, 138
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=790, 644, 630, 276, 083

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=63 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:5 (gap=45), P3:9 (gap=49)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 859: score=55.595033928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=54.79939642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 829: score=53.75348964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 929: score=53.198053571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 969: score=44.52921071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 857: score=43.07021071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 869: score=41.66027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 851: score=40.72040178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 989: score=40.36473928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 854: score=39.534007142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=852 sev=B
- 778: ds=833 sev=B
- 115: ds=826 sev=B
- 144: ds=817 sev=B
- 055: ds=795 sev=B
- 346: ds=769 sev=B
- 255: ds=752 sev=B
- 111: ds=742 sev=B
- 116: ds=722 sev=B
- 388: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=145 sev=red
  - 99: ds=49 sev=purple
  - 11: ds=27 sev=purple
  - 33: ds=26 sev=purple
  - 66: ds=22 sev=-
  - 77: ds=18 sev=-
  - 00: ds=7 sev=-
  - 55: ds=5 sev=-
  - 44: ds=2 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 39: ds=51 sev=blue
  - 45: ds=45 sev=blue
  - 28: ds=44 sev=blue
  - 49: ds=43 sev=blue
  - 14: ds=36 sev=purple
  - 47: ds=31 sev=purple
  - 58: ds=30 sev=purple
  - 37: ds=28 sev=purple
  - 12: ds=27 sev=purple
  - 68: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:713, 1:309, 6:141, 26:140, 34:84, 27:56, 15:53, 31:49, 18:48, 9:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=713 fs=0 fl=0 hz=0.0, 1:ds=309 fs=1 fl=1 hz=0.006172839506172839, 6:ds=141 fs=10 fl=4 hz=0.016726403823178016, 26:ds=140 fs=3 fl=2 hz=0.008174386920980927, 34:ds=84 fs=12 fl=3 hz=0.020053475935828877, 27:ds=56 fs=13 fl=3 hz=0.01904761904761905, 15:ds=53 fs=20 fl=1 hz=0.023732470334412083, 31:ds=49 fs=25 fl=3 hz=0.029850746268656716, 18:ds=48 fs=27 fl=0 hz=0.028846153846153848, 9:ds=45 fs=38 fl=1 hz=0.041666666666666664

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=61 flags=purple
- S17: ds=35 flags=purple
- S23: ds=32 flags=purple
- S20: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=2 last_repeat_gap=32 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=15), P2:5 (gap=22), P3:9 (gap=24)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 859: score=55.595033928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=54.79939642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 829: score=53.75348964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 929: score=53.198053571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 969: score=44.52921071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 857: score=43.07021071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 869: score=41.66027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 851: score=40.72040178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 989: score=40.36473928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 854: score=39.534007142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=966 sev=B
- 099: ds=916 sev=B
- 228: ds=813 sev=B
- 333: ds=796 sev=B
- 255: ds=763 sev=B
- 566: ds=739 sev=B
- 338: ds=733 sev=B
- 355: ds=728 sev=B
- 011: ds=706 sev=B
- 368: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=120 sev=red
  - 88: ds=72 sev=blue
  - 66: ds=70 sev=purple
  - 77: ds=41 sev=purple
  - 99: ds=24 sev=-
  - 44: ds=21 sev=-
  - 11: ds=13 sev=-
  - 00: ds=3 sev=-
  - 55: ds=2 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 57: ds=57 sev=red
  - 37: ds=51 sev=blue
  - 16: ds=47 sev=blue
  - 34: ds=45 sev=blue
  - 46: ds=37 sev=blue
  - 28: ds=36 sev=purple
  - 26: ds=35 sev=purple
  - 79: ds=30 sev=purple
  - 39: ds=25 sev=purple
  - 69: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:356, 16:198, 1:154, 34:139, 27:115, 26:102, 33:75, 13:72, 6:70, 29:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=356 fs=1 fl=1 hz=0.0056603773584905665, 16:ds=198 fs=4 fl=0 hz=0.008450704225352114, 1:ds=154 fs=4 fl=2 hz=0.011976047904191617, 34:ds=139 fs=13 fl=3 hz=0.01909307875894988, 27:ds=115 fs=14 fl=2 hz=0.019347037484885126, 26:ds=102 fs=0 fl=4 hz=0.006150061500615006, 33:ds=75 fs=22 fl=1 hz=0.026047565118912798, 13:ds=72 fs=21 fl=3 hz=0.026402640264026403, 6:ds=70 fs=18 fl=1 hz=0.02065217391304348, 29:ds=51 fs=27 fl=2 hz=0.03169398907103825

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=99 flags=purple
- S2: ds=82 flags=purple
- S15: ds=42 flags=purple
- S23: ds=41 flags=purple
- S7: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 126: score=1 tags=FLT
  - 136: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=36 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=38), P2:5 (gap=33), P3:9 (gap=36)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 859: score=55.595033928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=54.79939642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 829: score=53.75348964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 929: score=53.198053571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 969: score=44.52921071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 857: score=43.07021071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 869: score=41.66027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 851: score=40.72040178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 989: score=40.36473928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 854: score=39.534007142857135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=997 sev=B
- 228: ds=943 sev=B
- 337: ds=910 sev=B
- 145: ds=865 sev=B
- 016: ds=846 sev=B
- 066: ds=843 sev=B
- 777: ds=831 sev=B
- 388: ds=817 sev=B
- 588: ds=784 sev=B
- 227: ds=732 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=101 sev=blue
  - 11: ds=62 sev=purple
  - 00: ds=60 sev=purple
  - 55: ds=49 sev=purple
  - 22: ds=39 sev=purple
  - 99: ds=36 sev=purple
  - 33: ds=13 sev=-
  - 66: ds=11 sev=-
  - 77: ds=9 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 12: ds=119 sev=red
  - 35: ds=49 sev=blue
  - 39: ds=42 sev=blue
  - 59: ds=40 sev=blue
  - 49: ds=35 sev=purple
  - 45: ds=33 sev=purple
  - 19: ds=29 sev=purple
  - 29: ds=25 sev=purple
  - 13: ds=24 sev=-
  - 47: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:687, 35:245, 6:208, 28:180, 1:160, 17:113, 26:70, 5:53, 15:50, 4:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=687 fs=0 fl=2 hz=0.007168458781362007, 35:ds=245 fs=0 fl=3 hz=0.005657708628005658, 6:ds=208 fs=14 fl=2 hz=0.02077922077922078, 28:ds=180 fs=7 fl=0 hz=0.011335012594458438, 1:ds=160 fs=0 fl=0 hz=0.0, 17:ds=113 fs=17 fl=3 hz=0.022753128555176336, 26:ds=70 fs=3 fl=2 hz=0.007552870090634441, 5:ds=53 fs=22 fl=1 hz=0.027218934911242602, 15:ds=50 fs=26 fl=1 hz=0.028877005347593587, 4:ds=49 fs=23 fl=2 hz=0.028409090909090908

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=91 flags=blue+purple
- S19: ds=89 flags=red+purple
- S0: ds=66 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 228 -> evening:943(B); midday:813(B)
- 255 -> combined:752(B); midday:763(B)
- 288 -> combined:852(B); midday:966(B)
- 338 -> evening:687(B); midday:733(B)
- 388 -> combined:713(B); evening:817(B)
- 778 -> combined:833(B); evening:997(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:27(purple); evening:62(purple)
- 12 -> combined:27(purple); evening:119(red)
- 28 -> combined:44(blue); midday:36(purple)
- 33 -> combined:26(purple); midday:120(red)
- 37 -> combined:28(purple); midday:51(blue)
- 39 -> combined:51(blue); evening:42(blue); midday:25(purple)
- 45 -> combined:45(blue); evening:33(purple)
- 49 -> combined:43(blue); evening:35(purple)
- 88 -> combined:145(red); evening:101(blue); midday:72(blue)
- 99 -> combined:49(purple); evening:36(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(7.0272499999999996)[R1,Mirror-Echo], 9(6.3598928571428575)[R2,XVAR-Cons(CEM)], 1(1.7149999999999999)[R1,Double-Pressure], 6(0.9508)[R2,Double-Pressure], 3(0.7955714285714286)[R3,Mirror-Echo]
- P2: 5(8.642142857142858)[R1,XVAR-Cons(CEM)], 2(7.040799999999999)[R2,XVAR-Cons(CEM)], 6(1.871957142857143)[R3,XVAR-Cons(CE)], 8(0.2074857142857143)[R3,Swap]
- P3: 9(8.761071428571428)[R1,XVAR-Cons(CEM)], 7(1.7829642857142858)[R3,XVAR-Cons(CM)], 4(1.3646142857142856)[R2,Mirror-Echo], 1(1.044)[R2,Double-Pressure], 5(1.0135)[R2,Double-Pressure]

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
