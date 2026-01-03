# Master Validation Run Report — Connecticut4 — results 2025-06-21 (history workbook ~ 2025-06-20)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-21/Connecticut4/`
- Winners lens: `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/`
- Stable: `sharepacks/2025-06-21/Connecticut4/stable/Connecticut4/`
- Digit Reduction: `sharepacks/2025-06-21/Connecticut4/digit_reduction/Connecticut4/`
- VTRAC: `sharepacks/2025-06-21/Connecticut4/vtrac/Connecticut4/`
- Hot Zones: `sharepacks/2025-06-21/Connecticut4/hot_zones/Connecticut4/`
- Aux: `sharepacks/2025-06-21/Connecticut4/aux/Connecticut4/`
- Aux draws snapshot: `sharepacks/2025-06-21/Connecticut4/aux/draws/`

## Part A — Winners HTML/JSON (environment lens)
Winners HTML files (open in browser/editor):
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251201_233350.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_081747.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_133306.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_134109.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251209_181910.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251219_164349.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251201_233349.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_081746.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_133305.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_134108.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251209_181910.html`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251219_164349.html`

Winners JSON files:
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_081747.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_133306.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251206_134109.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251209_181910.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251219_164349.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_081746.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_133305.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251206_134108.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251209_181910.json`
- `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251219_164349.json`

Part A answers (fill using the template’s Part A questions):
- Primary files used (latest stamp):
  - `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251219_164349.html`
  - `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac5_winner_950_20251219_164349.json`
  - `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251219_164349.html`
  - `sharepacks/2025-06-21/Connecticut4/winners/Connecticut4/Connecticut4_vtrac2_winner_155_20251219_164349.json`

- Q1:
  - Set1 col1 ladders are “index-family heavy” (many `hit-family` tags) and, for the Midday winner 950 (canonical 059, VT index 5), they repeatedly contain **winner-family members** and many `hit-winner` tags (58 hit-winner cells across the full winners JSON, mostly Midday variant).
  - For the Evening winner 155 (VT index 2), the winners JSON shows only **1** `hit-winner` cell total, so Set1 col1 ladders do **not** meaningfully narrow to 155 on this day.
- Q2:
  - Col1/col2 persistence is very strong (lots of `*`/`**` survivors), but it’s asymmetric by draw:
    - Midday: the VT5 family is heavily present (persistent `hit-family` + many `hit-winner` tags), so the environment is “tight enough” to justify a small box.
    - Evening: heat exists, but it does not converge cleanly on the 155 family.
- Q3:
  - Last-survivor story (by winner-family stats in the VTRAC winners JSON digests):
    - Winner 950 family (idx5): dominant survivors are `559` (occ=36, pers=96), then `455`; the winner canonical `059` is present as a survivor (occ=3, pers=3) but **not** dominant; literal `950` has 0.
    - Winner 155 family (idx2): the winner has 0; dominant survivors are `506` (occ=7, pers=13), `001`, `105`.
  - VTRAC analyzer agrees on “last remaining 3‑VTRAC pressure” for Midday: idx5 is rank 2/35 (score ≈ 53.69).
- Q4:
  - Variant bias is clear:
    - Midday winner 950: strong representation as VT family / canonical survivor signals (winner index is #2 overall in VTRAC analyzer).
    - Evening winner 155: weak representation (winner index ranks 13/35; winner literal/canonical not present as a clean survivor).
- Q5:
  - Permutation lane clarity:
    - 950: literal `950` is not present in the VTRAC winners stats tables (literal=0), so the “perm lane” is not tight; the evidence is canonical/family-based → prefer boxed/VT coverage over perm-only.
    - 155: literal/canonical don’t show as clean survivors → perm lane is diffuse.
- Q6:
  - Environment verdict: **support** overall, but “strong-support for Midday / weak-noisy for Evening”.
- Q7:
  - Hot Zones overlap is strong for Midday and moderate for Evening:
    - `059` is rank 4/204 in `hot_zones_top_lanes.csv` and is present in the Hot Zones winner map (top20+guard).
    - `155` is rank 72/204 in `hot_zones_top_lanes.csv` (not in the top20 winner map, which is expected at that rank).
- Q8:
  - Cross-set carryover:
    - Winner 950: many `hit-winner` tags exist across Set2 → Set1 and across multiple Draw rows, indicating persistence as a family/canonical survivor.
    - Winner 155: essentially no carryover signal (1 cell total tagged).
- Q9:
  - Quick Aux-visible cues that also show up in the winners tables:
    - There are frequent `hit-family` tags (VT family density) and DR “long-string box” tags (`ls-box`) around the 950 family in Midday rows.
    - The Evening winner 155 has an obvious pair cue (contains `55`), which is overdue/repeating in Aux (logged in Part 3).
- Q10:
  - 4-hit-criteria viability:
    - Midday 950 (canon 059, idx5): Exact boxed is plausible (canonical is present and tool evidence later supports it); VT-boxed is plausible (idx5 is highly ranked). VT-straight is weaker (winner not in top index straights).
    - Evening 155 (canon 155, idx2): Exact paths are not supported by the winners lens; VT-boxed is the only coherent fallback.
- Q11:
  - Exact triple presence in string tables:
    - 950: literal `950` does not appear as a stand-alone cell value in the winners JSON tables, but canonical `059` does appear as draw_data cells in Evening/Combined (and many cells tagged `hit-winner` contain permutations like `590/059`).
    - 155: literal `155` does not appear as a stand-alone cell value; it only shows up embedded in a long survivor string (1 `hit-winner` tagged cell).
- Q12:
  - Profitable environment summary:
    - Midday has repeatable “profitable traits”: strong VT-family density, Hot Zones rank‑4 presence for `059`, and Stable later confirms a high-rank exact signal.
    - Evening lacks those traits; it’s a caution/noise environment.
- Q13:
  - Dominance vs dilution:
    - Midday winner family is present, but dominance is carried by sibling patterns (`559`, `455`) rather than the literal winner permutation.
    - Evening winner is diluted (0 occurrence in the family stats tables; siblings dominate).
- Q14:
  - Noise check:
    - Midday: comparatively clean (one strong VT-family signal plus Hot Zones overlap).
    - Evening: noisy (weak direct winner representation; multiple competing families/lanes).

---

## Part 2 — Tool-by-tool (paste blocks + answers)
Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.

### 2.Stable — Connecticut4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Stable Summary — Connecticut4 (2025-06-21)

## Midday winner 950 (canonical 059)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=27 | family_rows=142 | exact_boxed=27 | exact_straight=17 | vt_boxed=27
- Scores (patterns_scores.csv): rank 109/5835 (rank_frac 0.01868037703513282) | score 25.5 (top 33.5, ratio 0.7611940298507462, delta 8.0) | section Midday, Set Set1, Draw Draw4, Col 2, hot 2, vt_straight 2.0 | why straight|cov2|hp_repeat3|vstr2|mirror|hot2|hidden3v|vtrac_straight|set_chain2|draw_chain7
- Compound (patterns_compound.csv): rank 20/2063 (rank_frac 0.009694619486185167) | score 51.0 (top 81.0, ratio 0.6296296296296297, delta 30.0) | section Midday, col1_hits 1, hot2 4, set_chain 2, draw_chain 7 | why set_chain2|draw_chain7|col1x1|hot1x7|hot2x4|vstrx6
- Families (patterns_families.csv): count 42 | rank 301/1461 (rank_frac 0.20602327173169063) | score 21.0 (top 35.5, ratio 0.5915492957746479, delta 14.5) | section Combined, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=27

## Evening winner 155 (canonical 155)
- Spotlight (winner_family_spotlight_raw.csv): exact_canonical_rows=1 | family_rows=211 | exact_boxed=1 | exact_straight=1 | vt_boxed=1
- Scores (patterns_scores.csv): rank 5262/5835 (rank_frac 0.9017994858611825) | score 9.0 (top 33.5, ratio 0.26865671641791045, delta 24.5) | section Evening, Set Set1, Draw Draw7, Col 1, hot 0, vt_straight 2.0 | why straight|cov1|double_mirror|vtrac_straight
- Compound (patterns_compound.csv): rank 1370/2063 (rank_frac 0.664081434803684) | score 11.5 (top 81.0, ratio 0.1419753086419753, delta 69.5) | section Evening, col1_hits 1, hot2 0, set_chain 1, draw_chain 1 | why draw_chain1|col1x1|vstrx1|dblmirrorx1
- Families (patterns_families.csv): count 57 | rank 1/1461 (rank_frac 0.0006844626967830253) | score 35.5 (top 35.5, ratio 1.0, delta 0.0) | section Midday, hot2 0
- Metrics (metrics.json): exact_boxed=True | exact_straight=True | vt_boxed_count=24

## Top compound candidates (patterns_compound.csv)
- rank    1 | canon 344 | section Evening | score 81.0 | col1_hits 7 | hot2 11
- rank    7 | canon 446 | section Evening | score 66.5 | col1_hits 4 | hot2 9
- rank   14 | canon 0557 | section Midday | score 58.0 | col1_hits 5 | hot2 7
- rank    4 | canon 055 | section Midday | score 72.5 | col1_hits 5 | hot2 7
- rank    3 | canon 057 | section Midday | score 74.0 | col1_hits 6 | hot2 7
- rank   11 | canon 144 | section Evening | score 60.5 | col1_hits 5 | hot2 6
- rank    5 | canon 334 | section Evening | score 67.5 | col1_hits 1 | hot2 6
- rank    5 | canon 366 | section Evening | score 67.5 | col1_hits 1 | hot2 6
- rank    2 | canon 336 | section Evening | score 77.0 | col1_hits 2 | hot2 6
- rank   27 | canon 3344 | section Evening | score 48.0 | col1_hits 0 | hot2 6

## Top families (patterns_families.csv)
- rank 1454 | family 11 | score 4.0 | hot2 0 | section Midday
- rank  434 | family 12 | score 18.5 | hot2 0 | section Midday
- rank  551 | family 20 | score 17.0 | hot2 0 | section Midday
- rank  637 | family 1 | score 16.0 | hot2 0 | section Midday
- rank  698 | family 9 | score 15.5 | hot2 0 | section Midday

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Midday winner 950 (canon 059) is strongly present in brain outputs:
    - Scores: rank 109/5835 (top ~1.9%), score 25.5, section Midday, Set1 Draw4 Col2, `hot=2`, `vt_straight=2.0`.
    - Compound: rank 20/2063 (top ~1.0%), score 51.0, section Midday, strong set/draw chains.
    - Spotlight: exact_canonical_rows=27 with exact_boxed/exact_straight flags.
  - Evening winner 155 is present but not elevated:
    - Scores: rank 5262/5835 (bottom ~10%), score 9.0, section Evening, Set1 Draw7 Col1.
    - Families: winner family ranks 1/1461 (dominant family), but the specific winner triple is not top-ranked.
- Q2:
  - Midday: all 4-hit criteria are plausible via Stable (exact_boxed/exact_straight True; vt-boxed present; vt-straight tag present).
  - Evening: exact flags exist, but the placement is weak (low score/rank), so the practical path is “family/boxed”, not “tight straight”.
- Q3:
  - Stable winners artifacts align with brain evidence:
    - `validate_stable_winners.py` passes (spotlight coherent with metrics).
    - No sign of missing artifacts or dtype/leading-zero mismatch for this state/day.
- Q4:
  - Midday is a “dominant signal” inside Stable (winner is near the top of Scores/Compound).
  - Evening is noisy inside Stable: despite a dominant family, the winner triple itself is not prioritized.
- Q5:
  - Top compound candidates (highest overall) are dominated by Evening-side clusters: `344`, `336`, `446`, etc.
  - Midday winner `059` is still “keep-worthy” because it is high-rank in Scores + strong in Compound, even if not the absolute top compound row.
- Q6:
  - Evening miss pattern: winner family dominance exists, but the winner row lacks hot/chain reinforcement so it gets buried.
- Q7:
  - (V) Data/schema: OK (scores/compound/families/metrics/spotlight present; strict tables↔aux alignment already passed for this state/day).
  - (V) Winners artifacts: present; validator passes.
- Q8:
  - If we want Stable to act more like a “caller” on days like this, we may need a controlled boost for “family dominance” when the triple is present but low-ranked.
- Q9:
  - Cross-tool synergy seed (Midday): `059` is a rare case where winners lens + Stable + Hot Zones all align; that’s a prime “superbrain anchor candidate” pattern.
- Q10:
  - Key note: Stable can be simultaneously “excellent” (Midday) and “family-only” (Evening) on the same state/day; the workflow must record both as tool outcomes, not pipeline failures.

---

### 2.Digit Reduction — Connecticut4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Digit Reduction Summary — Connecticut4 (stamp 20251219)

## Midday winner 950 (canonical 059)
- Stamp (winner_stamp.json): items_total=294 | exact_any=112 exact_final=0 | vtrac_any=278 vtrac_final=0 | drop_exact_any=128 drop_exact_final=0 | drop_vtrac_any=294 drop_vtrac_final=0 | family_exact_any=2 family_exact_final=0 | family_vtrac_any=278 family_vtrac_final=0
- Flags (winner_flags.csv): rows=294 | exact_any=112 vtrac_any=278 | drop_exact_any=128 drop_vtrac_any=294 | family_exact_any=2 family_vtrac_any=278 | vt_boxed=20 vt_straight=0
- Hits (winner_hits.csv): rows=294 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=20 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=14 | winner_present=True | winner_best_rank=59 | winner_rank_fraction=4.214285714285714 | winner_score_v2=6.66381 top_score_v2=13.527143 | winner_score_ratio_to_top=0.49262508720429726 winner_score_delta_from_top=6.863333000000001
- Reducer scores present: True

## Evening winner 155 (canonical 155)
- Stamp (winner_stamp.json): items_total=13 | exact_any=0 exact_final=0 | vtrac_any=12 vtrac_final=0 | drop_exact_any=0 drop_exact_final=0 | drop_vtrac_any=1 drop_vtrac_final=0 | family_exact_any=0 family_exact_final=0 | family_vtrac_any=0 family_vtrac_final=0
- Flags (winner_flags.csv): rows=13 | exact_any=0 vtrac_any=12 | drop_exact_any=0 drop_vtrac_any=1 | family_exact_any=0 family_vtrac_any=0 | vt_boxed=1 vt_straight=0
- Hits (winner_hits.csv): rows=13 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=1 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=26 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=12.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Combined winner 950 (canonical 059)
- Stamp (winner_stamp.json): items_total=616 | exact_any=127 exact_final=0 | vtrac_any=583 vtrac_final=0 | drop_exact_any=155 drop_exact_final=0 | drop_vtrac_any=592 drop_vtrac_final=0 | family_exact_any=14 family_exact_final=0 | family_vtrac_any=502 family_vtrac_final=0
- Flags (winner_flags.csv): rows=616 | exact_any=127 vtrac_any=583 | drop_exact_any=155 drop_vtrac_any=592 | family_exact_any=14 family_vtrac_any=502 | vt_boxed=67 vt_straight=0
- Hits (winner_hits.csv): rows=616 | exact_final=0 vtrac_final=0 | drop_exact_final=0 drop_vtrac_final=0 | family_exact_final=0 family_vtrac_final=0 | vt_boxed=67 vt_straight=0
- Per-item (analyzer_v2_per_item.csv): best area_rank where exact_any=1 → 1 | best area_rank where vtrac_any=1 → 1
- Top candidates (analyzer_v2_top_candidates.csv): rows_total=22 | winner_present=False | winner_best_rank=None | winner_rank_fraction=None | winner_score_v2=None top_score_v2=17.677143 | winner_score_ratio_to_top=None winner_score_delta_from_top=None
- Reducer scores present: True

## Top per_item (analyzer_v2_per_item.csv)
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 2 | pattern 544 | score_v2 17.677143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 5 | pattern 594 | score_v2 13.577143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 3 | pattern 559 | score_v2 13.564921 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw5 col 2 | pattern 559 | score_v2 13.558571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 4 | pattern 594 | score_v2 13.527143 | match_types 
- area_rank 1 | variant Midday | section Midday | set Set1 draw Draw3 col 5 | pattern 559 | score_v2 13.527143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 4 | pattern 559 | score_v2 13.514921 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw6 col 2 | pattern 559 | score_v2 13.358571 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw3 col 3 | pattern 594 | score_v2 13.277143 | match_types 
- area_rank 1 | variant Combined | section Combined | set Set1 draw Draw4 col 2 | pattern 559 | score_v2 13.258571 | match_types 

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 544 | score_v2 17.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 594 | score_v2 13.577143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Combined | best_pattern 559 | score_v2 13.564921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Midday | best_pattern 559 | score_v2 13.527143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Combined | best_pattern 544 | score_v2 12.877143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 6 | variant Evening | best_pattern 544 | score_v2 12.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 7 | variant Midday | best_pattern 559 | score_v2 12.127143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 8 | variant Midday | best_pattern 554 | score_v2 11.777143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 9 | variant Combined | best_pattern 559 | score_v2 11.764921 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 10 | variant Evening | best_pattern 544 | score_v2 11.677143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Midday winner 950 (canon 059): DR reports `winner_present=True` but not as a strong top candidate (winner_best_rank=59 with top_score_v2=13.53).
  - Evening winner 155: `winner_present=False` (no direct candidate isolation).
  - Interpretation: DR sees the Midday winner as a weak/late candidate and doesn’t isolate the Evening winner at all.
- Q2:
  - Exact hits are not produced as “final hits” in DR (`exact_final=0`, `vtrac_final=0`), but VT-family presence is strong (vt_boxed_any is non-zero across variants).
- Q3:
  - DR winners artifacts are internally consistent (stamp ↔ flags ↔ hits): `validate_dr_winners.py` passes.
- Q4:
  - Inside DR, the environment is dominated by other patterns (`544`, `594`, `559`), and the winner is not a dominant candidate.
- Q5:
  - Top DR candidates are consistent across variants and heavily cluster on `544/594/559` (see embedded Top candidates list).
- Q6:
  - Miss analysis: DR appears to behave more like “family/coverage detector” here than a top‑N caller (especially for Evening).
- Q7:
  - (V) Schema/data OK; winners validator passes; no missing artifacts.
- Q8:
  - Optimization idea (log-only): if we keep DR as an evidence layer, we should treat “winner present but low” as a meaningful signal (timing/decay) rather than a failure.
- Q9:
  - Cross-tool synergy seed: DR’s dominant candidates (`559`) overlap the Midday winners lens “idx5 survivor” story, which reinforces the idea that “sibling dominance in-family” can still be profitable evidence.
- Q10:
  - Extra: DR is useful here as a sanity check that the “winner family exists in the candidate universe” even when DR doesn’t promote it into the top list.

---

### 2.VTRAC Analyzer — Connecticut4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# V-TRAC Summary — Connecticut4 (stamp 20251219_165151)

## Top indices (from enhanced JSON)
- index 23 | score 57.40263749999999 | features: presence=41.48513749999999, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 5 | score 53.690774999999995 | features: presence=38.883275, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 18 | score 49.2768725 | features: presence=35.9993725, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 8 | score 44.444914999999995 | features: presence=25.477415, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 33 | score 40.9452375 | features: presence=29.1777375, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 3 | score 32.73859999999999 | features: presence=20.561099999999996, cross_section=0.5, set_echo=0.6, first_hit=0.4
- index 13 | score 32.12785 | features: presence=19.16035, cross_section=0.5, set_echo=0.6, first_hit=0.33333333333333337
- index 12 | score 31.7517 | features: presence=19.8142, set_echo=0.3, first_hit=0.4, column_span=0.3375
- index 15 | score 25.188650000000003 | features: presence=16.521150000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2
- index 6 | score 24.898985000000003 | features: presence=13.941485000000002, cross_section=0.5, set_echo=0.6, first_hit=0.2666666666666667

## Top straights (from enhanced JSON)
590, 653, 563, 705, 907, 054, 536, 386, 683, 836

## Section summaries
- Midday: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Evening: hot=20 superhot=12 consensus_col1=False consensus_col2=False
- Combined: hot=20 superhot=12 consensus_col1=False consensus_col2=False

## Winners lens (from winners VTRAC report JSON/HTML)
- winner 155 | index 2 | file Connecticut4_vtrac2_winner_155_20251219_164349.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts
- winner 950 | index 5 | file Connecticut4_vtrac5_winner_950_20251219_164349.json | rank 0 score 0 | stats keys: pattern_occurrence, pattern_persistence, pattern_stability, straight_counts

## Winner index placement (in enhanced JSON rankings)
- winner 155 | index 2 rank 13/35 (rank_frac 0.37142857142857144) | score 21.470546666666667 (top 57.40263749999999, ratio 0.37403414898255627, delta 35.93209083333332) | winner_in_index_straights=False | top_index_straights: 056 (6.308), 065 (5.994), 506 (5.868)
- winner 950 | index 5 rank 2/35 (rank_frac 0.05714285714285714) | score 53.690774999999995 (top 57.40263749999999, ratio 0.9353363771830171, delta 3.711862499999995) | winner_in_index_straights=False | top_index_straights: 590 (15.326), 054 (13.208), 095 (10.924)
  - Note: winners lens lives under the winners sharepack and is generated post-results.

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Midday winner index 5 is strongly supported by the VTRAC analyzer: rank 2/35 (score ≈ 53.69; ratio-to-top ≈ 0.94).
  - Evening winner index 2 is mid-pack: rank 13/35 (score ≈ 21.47).
- Q2:
  - VT-boxed: plausible for Midday (idx5 is top-ranked).
  - VT-straight: weaker for both winners in this run (`winner_in_index_straights=False`).
- Q3:
  - Winners lens aligns with the analyzer: the Midday winner’s index is near-top; the Evening winner’s index is not.
- Q4:
  - Dominance inside VTRAC is clearer for Midday (idx5 pressure) than Evening (idx2 not dominant).
- Q5:
  - Top indices today: 23, 5, 18, 8, 33.
  - Top straights list includes `590` and `054` (both in the Midday winner’s idx5 family), reinforcing Midday’s family density story.
- Q6:
  - Miss analysis (Evening): idx2 being mid-ranked explains why an “idx2-only” strategy would be weak here without additional confirmation layers.
- Q7:
  - (V) VTRAC artifacts exist and are non-empty (compact report / enhanced JSON / summary).
- Q8:
  - Optimization note (log-only): treat “winner index strong but winner straight absent” as a boxed/perm-lane decision driver.
- Q9:
  - Cross-tool synergy seed: Midday is a clean synergy case (VTRAC idx5 + Stable exact + Hot Zones rank 4 on 059).
- Q10:
  - Extra: the VTRAC analyzer provides a strong day-level “which index is live” signal; it does not, by itself, resolve the permutation (straight) decision.

---

### 2.Hot Zones — Connecticut4 — 2025-06-21

0) Outputs reviewed
   - Brain: (see file list below)
   - Winners: (see file list below)
   - Missing brain?: none
   - Missing winners?: none

   Summarizer block (embedded from summary.md):

```markdown
# Hot Zones Summary — Connecticut4 (2025-06-21)

## Midday winner 950 (canonical 059)
- Top lanes (hot_zones_top_lanes.csv): present | rank 4/204 (rank_frac 0.0196078431372549) | score_mean 20.831 (top 22.029, ratio 0.9456171410413545, delta 1.1980000000000004)
- Per-lane (hot_zones_per_lane.csv): has_straight=True has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=True (scope top20+guard_hits, limit 20)

## Evening winner 155 (canonical 155)
- Top lanes (hot_zones_top_lanes.csv): present | rank 72/204 (rank_frac 0.35294117647058826) | score_mean 17.33 (top 22.029, ratio 0.7866902719142947, delta 4.699000000000002)
- Per-lane (hot_zones_per_lane.csv): has_straight=False has_vt_straight=True
- Winner map (hot_zones_winner_map.json/csv): file_present=True | triad_present=False (scope top20+guard_hits, limit 20)
- Notes: winner_not_in_top20_winner_map (expected when winner rank > 20)

## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)
- rank    1 | triad 012 | vt_triad 123 | score_mean 22.029 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    2 | triad 007 | vt_triad 13 | score_mean 21.186 | tags col1,funnel_precol1,hot12,hot16,hot20,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    3 | triad 366 | vt_triad 24 | score_mean 20.903 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_straight
- rank    4 | triad 059 | vt_triad 115 | score_mean 20.831 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    5 | triad 367 | vt_triad 234 | score_mean 20.802 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight
- rank    6 | triad 026 | vt_triad 123 | score_mean 20.792 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    7 | triad 139 | vt_triad 245 | score_mean 20.581 | tags col1,funnel_precol1,guard_set1,hot12,hot16,hot20,hot4,hot8,literal_draw,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank    8 | triad 336 | vt_triad 24 | score_mean 20.2 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical3,vertical4,vt_only_lane,vt_straight
- rank    9 | triad 344 | vt_triad 45 | score_mean 19.643 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vt_only_lane,vt_straight
- rank   10 | triad 057 | vt_triad 113 | score_mean 19.38 | tags col1,funnel_precol1,hot12,hot16,hot20,hot4,hot8,ls2_lane,ls_col_42,set1_bonus,straight_lane,superhot_set1,vertical1,vertical2,vertical3,vertical4,vt_only_lane,vt_straight

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Hot Zones captures both winners in `top_lanes`:
    - Midday canonical `059`: rank 4/204 (very strong; near-top).
    - Evening canonical `155`: rank 72/204 (present but not dominant).
- Q2:
  - Midday: has_straight=True and has_vt_straight=True → plausible straight-lane evidence exists for the 059 family.
  - Evening: vt-straight evidence exists, but the winner is not a high-ranked lane.
- Q3:
  - Winners artifacts are consistent: `validate_hot_zones_winners.py` confirms winners are present in `top_lanes`.
- Q4:
  - Midday is “dominant lane” inside Hot Zones (rank 4).
  - Evening is “noisy lane” (rank 72) and not present in top20 winner_map (expected at that rank).
- Q5:
  - Top lanes are heavily col1/funnel driven (rank 1 is `012`, and `059` is rank 4).
  - This suggests Hot Zones is emphasizing early columns (col1/col2 pressure) on this day.
- Q6:
  - Miss analysis (Evening): `155` is present but too low for a top‑20 map view; it would require either wider coverage or a “family confirmation” rule.
- Q7:
  - (V) Schema/data OK: `top_lanes`, `per_lane`, and `meta` exist; winners map exists.
- Q8:
  - Optimization note (log-only): ensure that “winner rank > 20” is recorded as expected (not a failure) when relying on a top‑20 winner map.
- Q9:
  - Cross-tool synergy seed: `059` appears as a top Hot Zones lane and is simultaneously a top Stable/VTRAC signal; that is the exact “stacked evidence” case the superbrain should favor.
- Q10:
  - Extra: Hot Zones is especially useful here as a “confirmation layer” for a Stable/VTRAC candidate (it independently surfaced `059` near the top).

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Midday: `059` / VT index 5 is the dominant cross-tool convergence (Stable high-rank exact + Hot Zones rank 4 + VTRAC idx5 rank 2/35).
  - The broader idx5 family dominance (`559`, `455`, `054`, `590`) is also consistent between winners lens and DR/VTRAC outputs.
- Conflicts/noise:
  - Evening: Stable shows “family dominance exists” (families rank 1) but the winner triple is low-ranked; VTRAC index2 is mid-pack and winners lens does not show strong survivor alignment.
- Aggregator/aux hooks to test next:
  - If (Stable rank_frac < ~0.02) AND (Hot Zones rank_frac < ~0.05) AND (winner index ranks top ~3), treat as “high-confidence box candidate” (Midday pattern here).
  - If (family dominance high) but (triple rank is poor), treat as “box-only / low-cost probe” (Evening pattern here).

## Part 3 — Aux Features (paste block + answers)
Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.

Aux draws snapshot dir: `sharepacks/2025-06-21/Connecticut4/aux/draws/`

0) Outputs reviewed
   - Draw CSV snapshot: (see aux draws folder)
   - Evidence dump: summary.md/summary.json

   Summarizer block (embedded from summary.md):

```markdown
# Aux Summary — Connecticut4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=763, 913, 201, 620, 070
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=913, 620, 221, 894, 438
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=763, 201, 070, 059, 778

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=3 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=14), P2:4 (gap=17), P3:7 (gap=22)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=936 sev=B
- 111: ds=920 sev=B
- 145: ds=895 sev=B
- 448: ds=837 sev=B
- 004: ds=828 sev=B
- 223: ds=809 sev=B
- 099: ds=800 sev=B
- 001: ds=783 sev=B
- 127: ds=782 sev=B
- 466: ds=735 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=163 sev=red
  - 88: ds=29 sev=purple
  - 44: ds=28 sev=purple
  - 55: ds=23 sev=-
  - 99: ds=21 sev=-
  - 11: ds=14 sev=-
  - 66: ds=11 sev=-
  - 77: ds=8 sev=-
  - 22: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 14: ds=85 sev=red
  - 03: ds=43 sev=blue
  - 56: ds=39 sev=blue
  - 04: ds=38 sev=blue
  - 15: ds=37 sev=blue
  - 47: ds=35 sev=purple
  - 68: ds=27 sev=purple
  - 27: ds=26 sev=purple
  - 57: ds=25 sev=purple
  - 17: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:168, 2:131, 4:81, 23:72, 8:66, 14:61, 10:45, 15:41, 6:39, 9:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=168 fs=16 fl=2 hz=0.022140221402214024, 2:ds=131 fs=17 fl=2 hz=0.02261904761904762, 4:ds=81 fs=25 fl=2 hz=0.029900332225913623, 23:ds=72 fs=17 fl=2 hz=0.021372328458942633, 8:ds=66 fs=43 fl=0 hz=0.04658721560130011, 14:ds=61 fs=31 fl=0 hz=0.033879781420765025, 10:ds=45 fs=17 fl=1 hz=0.022641509433962266, 15:ds=41 fs=17 fl=3 hz=0.02107481559536354, 6:ds=39 fs=31 fl=0 hz=0.03311965811965812, 9:ds=38 fs=35 fl=1 hz=0.03761755485893417

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=86 flags=red+purple
- S4: ds=66 flags=purple
- S12: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 027: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=31 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=25), P2:0 (gap=25), P3:7 (gap=12)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=891 sev=B
- 337: ds=854 sev=B
- 889: ds=824 sev=B
- 234: ds=775 sev=B
- 225: ds=751 sev=B
- 077: ds=732 sev=B
- 009: ds=725 sev=B
- 279: ds=698 sev=B
- 117: ds=684 sev=B
- 128: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=81 sev=blue
  - 11: ds=72 sev=blue
  - 00: ds=40 sev=purple
  - 44: ds=37 sev=purple
  - 77: ds=23 sev=-
  - 88: ds=14 sev=-
  - 55: ds=11 sev=-
  - 99: ds=10 sev=-
  - 66: ds=5 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 18: ds=90 sev=red
  - 69: ds=67 sev=red
  - 14: ds=42 sev=blue
  - 04: ds=34 sev=purple
  - 45: ds=30 sev=purple
  - 58: ds=30 sev=purple
  - 67: ds=26 sev=purple
  - 01: ds=25 sev=purple
  - 09: ds=25 sev=purple
  - 28: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:142, 13:123, 19:104, 23:90, 17:72, 2:65, 8:57, 27:49, 31:46, 5:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=142 fs=2 fl=0 hz=0.006006006006006006, 13:ds=123 fs=16 fl=1 hz=0.021013597033374538, 19:ds=104 fs=21 fl=1 hz=0.026284348864994027, 23:ds=90 fs=23 fl=1 hz=0.026402640264026403, 17:ds=72 fs=32 fl=2 hz=0.037158469945355196, 2:ds=65 fs=22 fl=1 hz=0.026713124274099886, 8:ds=57 fs=53 fl=0 hz=0.05644302449414271, 27:ds=49 fs=16 fl=3 hz=0.020452099031216364, 31:ds=46 fs=20 fl=3 hz=0.024390243902439025, 5:ds=43 fs=14 fl=2 hz=0.018046709129511677

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=92 flags=purple
- S6: ds=65 flags=red+purple
- S9: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 016: score=2 tags=RS
  - 034: score=2 tags=RS
  - 124: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=23 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=17), P2:3 (gap=36), P3:5 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 255: ds=933 sev=B
- 034: ds=910 sev=B
- 228: ds=888 sev=B
- 088: ds=886 sev=B
- 223: ds=847 sev=B
- 666: ds=835 sev=B
- 225: ds=810 sev=B
- 678: ds=711 sev=B
- 668: ds=708 sev=B
- 399: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=84 sev=blue
  - 88: ds=49 sev=purple
  - 55: ds=31 sev=purple
  - 99: ds=15 sev=-
  - 44: ds=14 sev=-
  - 66: ds=12 sev=-
  - 11: ds=7 sev=-
  - 22: ds=5 sev=-
  - 77: ds=4 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 35: ds=88 sev=red
  - 14: ds=77 sev=red
  - 15: ds=72 sev=red
  - 56: ds=72 sev=red
  - 16: ds=43 sev=blue
  - 08: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 57: ds=31 sev=purple
  - 39: ds=30 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 20:223, 2:171, 15:144, 32:130, 16:117, 34:93, 13:84, 4:55, 6:53, 33:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 20:ds=223 fs=18 fl=2 hz=0.0258732212160414, 2:ds=171 fs=19 fl=2 hz=0.02811244979919679, 15:ds=144 fs=14 fl=1 hz=0.01873536299765808, 32:ds=130 fs=2 fl=0 hz=0.004120879120879121, 16:ds=117 fs=2 fl=1 hz=0.005961251862891207, 34:ds=93 fs=20 fl=2 hz=0.025, 13:ds=84 fs=23 fl=3 hz=0.028540065861690448, 4:ds=55 fs=22 fl=1 hz=0.024918743228602384, 6:ds=53 fs=16 fl=1 hz=0.0196078431372549, 33:ds=49 fs=29 fl=0 hz=0.03176341730558598

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=93 flags=red+purple
- S8: ds=91 flags=red+purple
- S24: ds=70 flags=purple
- S20: ds=69 flags=purple
- S6: ds=57 flags=purple
- S2: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 044 -> combined:695(B); evening:703(B)
- 145 -> combined:895(B); evening:672(B)
- 223 -> combined:809(B); evening:847(B)
- 225 -> evening:810(B); midday:751(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:43(blue); evening:33(purple)
- 04 -> combined:38(blue); midday:34(purple)
- 14 -> combined:85(red); evening:77(red); midday:42(blue)
- 15 -> combined:37(blue); evening:72(red)
- 33 -> combined:163(red); evening:84(blue); midday:81(blue)
- 44 -> combined:28(purple); midday:37(purple)
- 47 -> combined:35(purple); evening:29(purple)
- 56 -> combined:39(blue); evening:72(red)
- 57 -> combined:25(purple); evening:31(purple)
- 88 -> combined:29(purple); evening:49(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.8864285714285716)[R1,XVAR-Cons(CM)], 3(2.8206857142857142)[R3,XVAR-Cons(CE)], 5(2.4252285714285717)[R2,XVAR-Cons(CM)], 8(1.3595714285714284)[R1,Mirror-Echo], 7(0.9552999999999999)[R2,Double-Pressure]
- P2: 3(3.4322857142857144)[R3,Mirror-Echo], 8(3.402457142857143)[R2,Mirror-Echo], 4(2.725207142857143)[R1,XVAR-Cons(CE)], 0(1.483607142857143)[R1,Mirror-Echo], 1(1.2433999999999998)[R2,Double-Pressure]
- P3: 5(6.764492857142857)[R2,XVAR-Cons(CEM)], 7(6.297507142857143)[R1,XVAR-Cons(CEM)], 6(2.3763714285714284)[R3,XVAR-Cons(CE)], 9(0.879)[R2,Double-Pressure]

```

Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):
- Q1:
  - Aux snapshot mode is history-aligned (`excel: data/history/Pick3StatsC4_2025_06_20.xlsm`) and strict alignment passed for this state/day:
    - `python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-21 --state Connecticut4 --strict` → OK.
  - Draw counts are n=1000 for each variant, and the newest draws listed in the Aux summary match the sharepack’s frozen world snapshot.
- Q2:
  - Positional pressure (high-level):
    - Combined top digits: P1=1, P2=4, P3=7; plus multiple cross-variant consensus notes.
  - Winner alignment:
    - 950 (digits 9/5/0): aligns weakly to positional tops, but digit 0 shows up in “double-pressure” notes (environmental support, not a direct call).
    - 155 (digits 1/5/5): aligns better (P1 has digit 1 consensus; P3 has strong digit‑5 consensus).
- Q3:
  - Positional shortlist (top candidates like `135/185/137/...`) does not directly contain `059` or `155`, but it does emphasize the “1/5 heavy” profile that matches the Evening winner’s digit structure.
- Q4:
  - Repeat-watch:
    - current_index=21 (streak=1) for Combined/Evening; neither winner index matches the repeat index (winners are idx5 and idx2).
- Q5:
  - VTRAC overlay / heatboard:
    - Combined overdue list includes idx2 and idx5 (both winners’ indices are “pressure-visible”).
    - Evening overdue list includes idx2 strongly (aligns with the 155 winner’s index context).
- Q6:
  - Doubles/pairs:
    - Winner 155 contains pair `55`, which is present as a repeating pair signal in Evening (purple) and Combined.
    - Winner 059/950 does not align to the top overdue doubles list (so Aux “doubles” is not the driver for Midday here).
- Q7:
  - Sums: due/flagged sums listed are not a direct match driver for either winner (059 sum=14; 155 sum=11).
- Q8:
  - Blackapple does not align with either winner on this day (top BA candidates do not include 059/155).
- Q9:
  - Aux convergence (lightweight table; signals counted: `idxTop`, `pair`, `pos`, `BA`):

    | candidate | canonical | idx | idxTop | pair | pos | BA | notes |
    |---|---:|---:|---:|---:|---:|---:|---|
    | 950 | 059 | 5 | ✓ (Combined idx5 overdue) | - | - | - | strong tool convergence instead of Aux |
    | 155 | 155 | 2 | ✓ (Combined+Evening idx2 overdue) | ✓ (`55`) | ~ | - | best Aux support is “idx+pair” |
    | 559 | 559 | 5 | ✓ | ✓ (`55`) | - | - | dominant in-family survivor in winners lens |
    | 544 | 445 | 9 | ? | ✓ (`44`) | - | - | DR top candidate; pair support only |
    | 590 | 059 | 5 | ✓ | - | - | - | VTRAC straight-family member of idx5 |
- Q10:
  - Aux application recommendation:
    - Use Aux as candidate-level boosts (idx pressure + pair pressure) rather than as a day-level gate on this state/day.
    - Cheapest reasonable play:
      - Midday: box `059` (evidence stack: Stable+Hot Zones+VTRAC).
      - Evening: if forced to play, a low-cost box on `155` is justifiable (pair support + family dominance), but the environment is noisy and “skip” is also defensible.

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
  - `059` (winner canonical) — Stable rank 109/5835 + Hot Zones rank 4/204 + VTRAC idx5 rank 2/35.
  - `559` — dominant in-family survivor in winners lens; DR top candidate.
  - `455` — strong in-family survivor in winners lens.
  - `054` / `590` / `095` — VTRAC idx5 straight-family members (appear in top straights list).
- Candidate universe (Evening):
  - `155` (winner canonical) — weak environment, but Stable exact flags exist; Hot Zones rank 72/204; Aux pair `55`.
  - `506` — dominant survivor inside idx2 family stats tables (winners lens).
  - `056` / `065` — top index2 straights (VTRAC analyzer).
  - `012` — Hot Zones top lane (rank 1) and a strong “col1 funnel” day marker.
  - `344` — top Stable compound candidate (environmental dominance).
- Evidence vectors:
  - Midday: the evidence stack is unusually clean for `059` (Stable exact + Hot Zones + VTRAC index), making it the anchor candidate.
  - Evening: evidence is fragmented; candidates are “plausible,” but not convergent.
- Coverage mapping + pack decision:
  - Midday:
    - Prefer boxed over perm-only because literal `950` does not show as a tight perm lane.
    - Pack: box `059` (6 combos) → would cover Midday winner `950` boxed.
  - Evening:
    - If playing: boxed `155` (6 combos) is the cheapest “evidence-respecting” play; full VT-boxed is not justified by evidence strength.
    - If passing: record as “skip/noisy environment” (also defensible).

---

## Part 5 — Overall Summary (key insights + fix/future hooks)
Use Part 5 prompts in the master template to summarize:
- Pack vs winners (post-hoc)
- Key environment tags
- What drove the win (best evidence)
- Conflicts/miss patterns + fix-now vs fix-later

Part 5 notes / answers:
- Pack vs winners:
  - Midday: box `059` covers winner `950` (boxed hit).
  - Evening: box `155` covers winner `155` (boxed hit) — but note the environment lens did not strongly support it (this is a “low-confidence hit” example).
- Key tags:
  - Midday: `Stable-exact`, `HotZones-top4`, `VTRAC-idx5-top2`, `idx5-family-dominance`.
  - Evening: `pair-55`, `family-dominance-but-low-rank`, `noisy-lane`.
- Drivers:
  - Midday winner was driven by true cross-tool convergence on `059/idx5`.
  - Evening winner is better explained by “family/pair pressure” than by clean string-table convergence.
- Conflicts:
  - Evening draw: VTRAC analyzer and winners lens did not strongly elevate idx2/155, while Stable/Hot Zones still had it present (low ranked).
- Fix-now vs fix-later:
  - Fix-now: none (alignment + validators pass; artifacts present).
  - Fix-later: consider a rule for “dominant family but low triple rank” days (cheap box probes vs skip).
- Next run:
  - Connecticut shows a strong Midday convergence and a weak Evening environment; compare against a state/day where both draws converge cleanly to test whether the “box anchor” logic generalizes.
