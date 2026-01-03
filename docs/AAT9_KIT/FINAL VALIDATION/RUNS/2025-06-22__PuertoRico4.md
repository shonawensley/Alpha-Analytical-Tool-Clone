# Master Validation Run Report — PuertoRico4 — results 2025-06-22 (history workbook ~ 2025-06-21)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-22/PuertoRico4/`
- Winners lens: `sharepacks/2025-06-22/PuertoRico4/winners/PuertoRico4/`
- Stable: `sharepacks/2025-06-22/PuertoRico4/stable/PuertoRico4/`
- Digit Reduction: `sharepacks/2025-06-22/PuertoRico4/digit_reduction/PuertoRico4/`
- VTRAC: `sharepacks/2025-06-22/PuertoRico4/vtrac/PuertoRico4/`
- Hot Zones: `sharepacks/2025-06-22/PuertoRico4/hot_zones/PuertoRico4/`
- Aux: `sharepacks/2025-06-22/PuertoRico4/aux/PuertoRico4/`
- Aux draws snapshot: `sharepacks/2025-06-22/PuertoRico4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
_No winners HTML found in the winners sharepack folder._

_No winners JSON found in the winners sharepack folder._

Part A answers (fill using the template’s Part A questions):
- Q1: N/A — no winners HTML/JSON were generated for Puerto Rico on this results date (there is no Puerto Rico line in `data/results/2025-06-22.txt`).
- Q2: N/A — without winners lens tables, we can’t assess Set1 ladder lanes or survivor narratives for a specific winner.
- Q3: N/A — no winner tagging possible (no winners overlay artifacts for this date).
- Q4: Environment proxy (tool-based, since winners are missing):
  - Stable top compounds are heavily concentrated in Evening section and dominated by `244/447/007/004/009` style canonicals.
- Q5: Permutation lane clarity (proxy):
  - Strong “0/2/4/4” cluster shows up across Stable + DR, suggesting a tight lane universe for candidate generation (but not gradeable without results).
- Q6: Environment verdict:
  - Treat this as a **pre-results snapshot only** (candidate universe capture), not an evaluable “did we hit” day.
- Q7: Hot Zones (proxy):
  - Top lanes include `155` (vt_triad 12) and `168` (vt_triad 224), aligning with the `224/244` theme.
- Q8: Cross-set carryover: N/A (no winners grading lens).
- Q9: Aux quick lens:
  - Positional top digits: Combined `0/3/4`, Midday `3/3/6`, Evening `7/0/0`.
  - Blackapple score=1 with floating digits `2/4` and `pairs.remaining_count=0` (context only).
- Q10: 4 hit criteria viability: N/A (no results/winners to grade).
- Q11: Exact triple presence: N/A (no winners overlays).
- Q12: “Profitable environment” summary:
  - This looks like a potentially strong **lane-dominance** environment (224/244/024-family), but we can’t validate without results.
- Q13: Dominance vs dilution:
  - Dominance is present (stable+DR concentrate on a small set of canonicals), but cannot be evaluated for dilution vs winners.
- Q14: Noise check:
  - No pipeline integrity issues (alignment guard passes); the missing winners lens is expected given missing results data for this state/day.

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — PuertoRico4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: PuertoRico4_winner_family_spotlight_raw.csv, PuertoRico4_winner_family_spotlight_families.csv

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — PuertoRico4 (2025-06-22)

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
  - No winners overlays exist for this state/day, so Stable cannot be graded for hit/miss.
- Q2: 4 hit criteria mapping
  - N/A (no winners/results for grading).
- Q3: Winners output alignment
  - Stable brain outputs are present; “missing winners” files are expected when `data/results/<D>.txt` lacks the state line.
- Q4: Dominance / noise
  - Very strong dominance in top compounds: `244`, `447`, `007`, `004`, `009`, plus expanded canonicals like `0244`.
- Q5: Candidate universe takeaways
  - A compact “box candidate” universe suggested by Stable would start around: `244`, `447`, `007`, `004`, `009`, `249`.
- Q6: Miss analysis
  - N/A (no results/winners to grade).
- Q7: Validation checks (V)
  - Outputs present; no missing brain artifacts.
- Q8: Optimization notes
  - None now; keep this as an “environment snapshot” example until we have results for PR on some D.
- Q9: Cross-tool synergy seed
  - Stable’s `244/224/024` dominance aligns with DR’s top candidates (`224/244/924`) and VTRAC top straights (`024/240/204/924`).
- Q10: Analyst’s extra insight
  - PuertoRico4 is still useful without winners: it helps define what a “high dominance lane day” looks like across Stable+DR+VTRAC.

---

### 2.Digit Reduction — PuertoRico4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: analyzer_v2/winners/*winner_map*.json, analyzer_v2/winners/*winner_flags*.csv, analyzer_v2/winners/*winner_hits*.csv

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — PuertoRico4 (stamp N/A)

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
  - No winners overlays exist for this state/day, so DR cannot be graded for hit/miss.
- Q2: Brain-only interpretation
  - DR strongly favors a small candidate cluster: top per_item and top candidates are dominated by `224`, `244`, and `924`.
- Q3: 4 hit criteria mapping
  - N/A (no results/winners to grade).
- Q4: Dominance / noise
  - This is a high-dominance DR day (candidate space concentrates heavily on a few triads).
- Q5: Candidate universe takeaways
  - Candidate triads suggested: `224`, `244`, `924` (and related 0/2/4 permutations).
- Q6: Miss analysis
  - N/A (no results/winners).
- Q7: Validation checks (V)
  - Brain outputs present; missing winners overlays are expected given missing results.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - DR’s `224/244` dominance agrees with Stable compounds (`244/0244`) and with VTRAC’s straights list including `024/240/204/924`.
- Q10: Analyst’s extra insight
  - This is a good candidate for “pre-results candidate pack design” (Part 4), but cannot be scored post-hoc until PR results exist for some D.

---

### 2.VTRAC Analyzer — PuertoRico4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: *vtrac*_winner_*.json, *vtrac*_winner_*.html

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — PuertoRico4 (stamp 20251221_222528)

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

## Winners lens
- No winners VTRAC report JSONs found alongside this analyzer sharepack.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1: Winners evidence vs brain outputs
  - No winners VTRAC report JSONs exist for this state/day → cannot grade.
- Q2: Brain-only interpretation
  - Very strong top indices (index 12, 3, 31, 5…) with high presence; top straights include `024/240/204/924`.
- Q3: 4 hit criteria mapping
  - N/A (no winners/results).
- Q4: Dominance / noise
  - VTRAC analyzer indicates a high-confidence index environment, but it’s not evaluable without results.
- Q5: Candidate universe takeaways
  - Use top straights as the “lean” universe: `024, 240, 204, 924, 092, 047, 407, 290, 524, 245`.
- Q6: Miss analysis
  - N/A (no winners/results).
- Q7: Validation checks (V)
  - Analyzer outputs present; missing winners lens is expected for this day.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Aligns strongly with Stable+DR on the `024/224/244/924` structure.
- Q10: Analyst’s extra insight
  - This is an ideal day to test “candidate-set compression” rules (how to go from index + stable + DR into a small box/straight hedge).

---

### 2.Hot Zones — PuertoRico4 — 2025-06-22

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — PuertoRico4 (2025-06-22)

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
  - No winners to grade; interpret Hot Zones as an environment map only.
- Q2: Brain-only interpretation
  - Top lanes are dominated by vt_triad 12/224/44/255 and include triads like `155`, `006`, `168`, `469`.
- Q3: 4 hit criteria mapping
  - N/A (no results/winners).
- Q4: Dominance / noise
  - Strong dominance in top lanes (clear ordering); not evaluable vs outcomes.
- Q5: Candidate universe takeaways
  - Consider the top-10 lanes as a compact triad universe: `155, 469, 338, 168, 006, 566, 019, 166, 149, 118`.
- Q6: Miss analysis
  - N/A (no results/winners).
- Q7: Validation checks (V)
  - Outputs present.
- Q8: Optimization notes
  - None now.
- Q9: Cross-tool synergy seed
  - Hot Zones has vt_triad 224 (triad 168), matching DR’s `224` focus.
- Q10: Analyst’s extra insight
  - Use Hot Zones here as a “vote” for which triads within the 0/2/4 universe deserve the most attention when designing a small pack.

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Strong convergence on a compact universe: `224/244/024/924` appears in Stable, DR, VTRAC straights, and Hot Zones vt_triad references.
- Conflicts/noise:
  - Not gradeable: no Puerto Rico results line for D=2025-06-22 → no winners overlays.
- Aggregator/aux hooks to test next:
  - Keep this sharepack as an “environment-only” example for pack design rules (how to compress to a playable set when multiple tools agree).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-22/PuertoRico4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — PuertoRico4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=551, 910, 383, 795, 656
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=910, 795, 681, 469, 708
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=551, 383, 656, 321, 913

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
    - combined: `sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` (n=1000)
    - midday: `sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` (n=1000)
    - evening: `sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` (n=1000)
  - Workbook provenance: `data/history/Pick3StatsC4_2025-06-21.xlsm` (aux_state_label=Puerto Rico).
  - Alignment guard: `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-22 --state PuertoRico4 --strict` → OK.
- Q2:
  - Positional pressure (by variant):
    - Combined top digits: `0/3/4`
    - Midday top digits: `3/3/6`
    - Evening top digits: `7/0/0`
- Q3:
  - Positional shortlist is dominated by `234/244/274/...` lanes, consistent with the `224/244` environment.
- Q4:
  - Repeat watch indicates:
    - Combined current_index=2; Midday current_index=9; Evening current_index=2.
- Q5:
  - VTRAC overlay top overdue indices: `33, 4, 26, 3, 29, 23, 20, 1, 35, 14` (Combined section).
- Q6:
  - Doubles/pairs pressure exists, but without results we can only treat it as “busy vs calm” context.
- Q7:
  - Sums are broadly flagged (purple / red+purple) → low discrimination by itself.
- Q8:
  - Blackapple score=1 (floating digits `2/4`, pairs_remaining=0) aligns with the 2/4-heavy environment, but is not gradeable here.
- Q9:
  - Cross-variant alerts show multi-variant pair/double pressure; treat as context only.
- Q10:
  - Aux supports the same compact universe the tools are pointing at; keep this as a pack-design training example until PR results are available for some D.

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
  - Candidate core: `224/244/024/924` families (from Stable+DR+VTRAC).
  - Lean hedge option: play VTRAC straights list from analyzer (`024/240/204/924/...`) rather than expanding broadly.
- Candidate universe (Evening):
  - Similar to Midday (tools are dominated by the same compact universe); keep spend tight.
- Evidence vectors:
  - Stable top compounds heavily favor `244/447/007/004/009`.
  - DR top candidates heavily favor `224/244/924`.
  - VTRAC top straights include `024/240/204/924`.
  - Hot Zones top lanes include vt_triad 224.
- Coverage mapping + pack decision:
  - Box-first posture for `224` and `244` (small perms), plus a small VTRAC-straight hedge (8 straights) if you want a lane-index hedge.
  - Not evaluable post-hoc for this D due to missing results.

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - N/A (no results/winners for PR on D=2025-06-22).
- Key tags:
  - Strong compact lane dominance: 2/4-heavy environment across Stable+DR+VTRAC+Hot Zones.
- Drivers:
  - Agreement across tools (dominant canonicals + straights) is the key takeaway.
- Conflicts:
  - Missing results line prevents any hit/miss grading.
- Fix-now vs fix-later:
  - Fix-now: none (alignment guard passes).
  - Fix-later: decide whether PR “missing results days” should be skipped automatically in report generation (to reduce confusion).
- Next run:
  - Continue D=2025‑06‑22 reports (SouthCarolina4 next); treat PuertoRico4 as “environment-only” for this D.
