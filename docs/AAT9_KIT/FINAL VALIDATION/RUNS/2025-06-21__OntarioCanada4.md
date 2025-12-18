# Master Validation Run Report — OntarioCanada4 — results 2025-06-21 (history workbook ~ 2025-06-20)

Reference template:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Sharepack pointers:
- Sharepack root: `sharepacks/2025-06-21/OntarioCanada4/`
- Winners lens: `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/`
- Stable: `sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4/`
- Digit Reduction: `sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4/`
- VTRAC: `sharepacks/2025-06-21/OntarioCanada4/vtrac/OntarioCanada4/`
- Hot Zones: `sharepacks/2025-06-21/OntarioCanada4/hot_zones/OntarioCanada4/`

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

Primary files used (latest stamp):
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251209_181934.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac21_winner_678_20251209_181934.json`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251209_181936.html`
- `sharepacks/2025-06-21/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac7_winner_517_20251209_181936.json`

- Q1:
  - Set1 col1 is extremely hot across *both* winner lenses and all variants: 24/28 Set1 (R2/R4/R6/R8) cells have a star marker; 20/28 are `**` (super-hot).
  - **678 / index 21**: Set1 col1 reads as “high pressure” for family-gap + long-string overlap (lots of `hit-family-gap` / `ls-box` tags), but the *winner itself* does not sit cleanly in Set1 col1 (no literal 678; winner perms show up mostly in earlier sets/other columns). Example of Set1 col1 still carrying winner-adjacent tags: Midday `Set1 Draw7 R6 col1 = 6687005599334` tagged `hit-winner`.
  - **517 / index 7**: same Set1 col1 heat pattern, but the winner’s visible perm lane is not “col1-led” (winner perm shows up in R6, mid-cols). So: col1 ladders are a strong environment signal, not a guarantee that the exact winner sits in col1.
- Q2:
  - Col1/col2 persistence is very strong: Set1 col2 is also 20/28 `**` across variants, indicating dense “most-recent” heat.
  - This appears to be an “always hot” Ontario Set1 phenomenon for this date (it’s identical in both winner JSONs), so it’s valuable as a *macro environment* signal (high persistence pressure), but not sufficient alone for literal extraction.
- Q3:
  - **678 / index 21 — dominant survivors (from stats)**:
    - Occurrence leaders: `367` (12), `362` (11), then `867` (3). Persistence leader: `362` (27), then `367` (14).
    - Interpreting “last surviving VT family patterns”: `367` (in index21 family), `867` (winner-perm), and `263` (perm of family member `236`) are the cleanest “family survivors” visible in stats/cells.
    - Relationship to draw_data: `367` appears directly in Evening draw_data col2 repeatedly (e.g., `Set1 Draw1..Draw6 draw_data col2=367`) and shows strongly in Combined; `362` appears in strings across all variants.
  - **517 / index 7 — dominant survivors (from stats)**:
    - Occurrence/persistence leader: `175` (occ 6, pers 14). Secondary: `256` (occ 2, pers 4). Also `701` and `170` show up lightly.
    - “Family survivors”: `175` (perm lane for 517’s boxed family), plus `256` and `701/170` (index7 family members) = a very tight family footprint.
    - Cross-variant: the `175` lane shows in Midday+Combined strings but is absent from the Evening table, which is a key cross-variant “hidden lane” insight for this winner.
- Q4:
  - **678 / index 21**: strongest winner tagging is in **Midday** (hit-winner cells: Midday 20 vs Evening 2 vs Combined 3). However, the family leader `367` shows primarily in **Evening+Combined** (367 substring hits: Evening 8, Combined 12, Midday 0). That’s a “winner digits show in Midday, family pressure shows in Evening/Combined” split.
  - **517 / index 7**: strongest winner tagging is in **Combined** (hit-winner cells: Combined 6 vs Midday 3 vs Evening 0). This supports the idea that “Combined often carries the perm lane even when the draw is Evening.”
- Q5:
  - **678 / index 21**: only a subset of winner permutations are actually present as substrings in the table strings: `867` and `687` dominate (25 total substring hits; by perm: `867`=13, `687`=11, `786`=1; no `678` literal). This is a “tight perm lane” rather than “full permutation scatter.”
  - **517 / index 7**: even tighter — only `175` appears as a substring (9 hits), and none of `517/157/571/715/751` appear. This strongly suggests a “one-perm lane day”.
- Q6:
  - Overall verdict: **strong persistence pressure but winner not literal**.
    - Strong: Set1 col1/col2 super-hot density + heavy family-gap tagging.
    - Weak (for cheap exact): neither winner appears as a clean literal triad in the table cells; both show via specific perm lanes embedded in longer strings.
    - Practical read: better environment for **VT-boxed / perm-lane extraction** than for “literal exact-only” plays.
- Q7:
  - Yes (notably for 678/index21): the same family anchor `367` that dominates the winners stats also shows up as a high-quality lane candidate in Hot Zones later (Part 2: Hot Zones top lanes includes triad `367` in Top 10). This is strong evidence that “Hot Zones lanes and VTRAC family leaders are converging”.
- Q8:
  - Cross-set carryover is real:
    - **678/index21** hit-family tags appear across Set3→Set2→Set1 in Midday (Set3 9, Set2 10, Set1 11) and Combined (Set3 8, Set2 6, Set1 17). So the family signal is not isolated to one set.
    - **517/index7** hit-family tags are heavily concentrated in Set1 Midday (Set1 23 vs Set2 6 vs Set3 2), which matches the observation that this winner is a late/set1-style perm lane.
- Q9:
  - The strongest “aux-adjacent” cue visible in the winners lens is the **long-string (Digit Reduction) box overlap**: both winner reports show `ls-box`/`ls-box-edge` tags heavily (78 each). This supports using DR/long-string features as a “support layer” for these days.
  - No explicit doubles/mirror tags exist in this winners lens; defer detailed Aux scoring to Part 3.
- Q10:
  - **Exact boxed**: plausible *only* via perm lane presence (e.g., 678 via `867/687`, 517 via `175`). Not via literal winner sitting cleanly.
  - **Exact straight**: looks weak from this lens (no `678` or `517` literal substring hits).
  - **VT-boxed** (boxed index family): strong conceptual path for both (678 is index21; 517 is index7), with strong family survivors (`367` for index21; `175/256/701` for index7).
  - **VT-straight** (8-straight lane): no `hit-vt-straight` tags appear in either report; treat VT-straight as not directly signaled by this lens here.
- Q11:
  - Literal exact triple presence is **not observed** as a clean triad in cells (no cell equals 678/517; and no substring hits for 678/517).
  - What *is* present is the boxed/permutation lane embedded in strings:
    - 678 shows via `867/687` substrings (25 total hits).
    - 517 shows via `175` substrings only (9 hits).
  - This supports your goal: measure when we can “play only the in-table perms” vs “pay for the full VT-box”.
- Q12:
  - Profitable-environment traits for this example:
    - Set1 col1/col2 super-hot density (20/28 `**` each) = high persistence pressure.
    - Strong family-gap coverage (`hit-family-gap` dominates tag counts: 156 for index21 view; 118 for index7 view).
    - Winner manifests through a **small perm lane**, not literal triad presence (cheap-focus opportunity if we can reliably detect which perm lane is “the one”).
    - Cross-variant “split”: family anchors can live in Evening/Combined even when the draw is Midday (and vice versa).
- Q13:
  - **678/index21**: partial dominance — `367` (family member) is top occurrence, but `362` (non-family) is almost equally dominant and is the top persistence leader. So: strong but not purely family-dominated.
  - **517/index7**: strong dominance — `175` (family perm lane) is clearly the leader, with only a few secondary survivors.
- Q14:
  - Environment looks **relatively clean** in “survivor count” terms (678 view has 7 nonzero patterns; 517 view has 4).
  - Main caution flag: cross-variant dispersion (e.g., 367 absent in Midday but dominant in Evening/Combined for the 678 view) — meaning a single-variant-only read can miss the best family anchor.

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
- Q1:
  - Midday winner 678 (canonical 678):
    - Winners artifact (spotlight): 14 rows; exact_boxed=14; exact_straight=7; vt_boxed=14.
    - Brain evidence:
      - `patterns_scores.csv`: rank 365 (Midday / Set3 Draw1 / Col4), score 21.0, why `boxed|cov4|hp_repeat3|vstr2|hot1|perm3|set_chain3`.
      - `patterns_compound.csv`: rank 141 (Midday), score 29.0, why `set_chain3|draw_chain3|col1x1|hot1x1|vstrx1`.
      - `metrics.json`: exact_boxed=True, exact_straight=True, vt_boxed_count=93.
  - Evening winner 517 (canonical 157):
    - Winners artifact (spotlight): 13 rows; exact_boxed=9; exact_straight=9; vt_boxed=13.
    - Brain evidence:
      - `patterns_scores.csv`: rank 3100 (Combined / Set3 Draw1 / Col7), score 12.0, why `straight|cov1|hp_repeat3|set_chain3`.
      - `patterns_compound.csv`: rank 598 (Combined), score 16.5, why `set_chain3|draw_chain1`.
      - `metrics.json`: exact_boxed=True, exact_straight=True, vt_boxed_count=50.
- Q2:
  - Exact boxed: **Yes** (both winners flagged exact_boxed=True; spotlight confirms).
  - Exact straight: **Yes** (both winners flagged exact_straight=True; spotlight confirms).
  - VT-boxed: **Yes** (spotlight vt_boxed counts; metrics vt_boxed_count non-trivial).
  - VT-straight: Not explicitly surfaced as a separate “hit” in this summary, but the why-tags (`vstr2`, `vstrx1`) show Stable is already using a VT-straight-related feature in scoring.
- Q3:
  - Winners artifacts (spotlights) align with the existence of winners inside Stable’s universe (it can “see” and tag them).
  - The mismatch is *ranking*: winners are present but not necessarily top-ranked (especially canonical 157 at rank 3100 in scores). This is important for Part 2: Stable currently behaves more like a “coverage + evidence” lens than a strict “top-N winner” predictor.
- Q4:
  - The strongest Stable compound candidates are not the winners (e.g., compound rank 1 is canon 229 with score 92.5). This suggests the environment is “busy” under Stable’s compound scoring, even though winners still get flagged as exact/vt_boxed.
- Q5:
  - Top compound clusters (highest scores): 229, 9, 225, 224, 259, 239, 59 (see embedded summary list).
  - Notable alignment to other tools:
    - `259` is also a top straight in the VTRAC analyzer brain (Part 2 VTRAC “Top straights”), which makes it a good cross-tool candidate even though it’s not the winner.
- Q6:
  - Stable did not “miss” winners in the sense of hit-flagging, but it **under-prioritized** them in the ranked outputs (especially canonical 157).
  - Likely causes (hypothesis to track, not a code change yet):
    - Compound scoring heavily favors col1_hits + hot2 density, which may surface “obvious heat” clusters (229/9/225/259…) over the perm-lane winners we saw in Part A.
    - The canonical-vs-literal mapping (517→157) can make “why it won” harder to see unless we always normalize in the report.
- Q7:
  - (V) Data read/schema OK: Yes (no missing artifacts; summary generated cleanly).
  - (V) Features/columns missing/zero: None observed here.
  - (V) Winners/metrics written: Yes (`metrics.json` + spotlight CSVs exist).
- Q8:
  - Most promising tuning direction (log as action item): lift/boost Stable’s scoring weight when Part A indicates a “tight perm-lane day” (e.g., 517→only 175 showing; 678→mostly 867/687) so those winners aren’t buried under generic hot2/col1 pressure.
  - Add reporting clarity (already handled by summary): always show literal + canonical together (e.g., 517→157), to avoid mis-reading the tool as “missing” winners.
- Q9:
  - Use Stable as a “high-confidence confirmation” signal when it flags exact_boxed/exact_straight, even if ranked low.
  - Cross-tool aggregator seed: if Stable flags a winner family + VTRAC winner lens shows a tight perm lane, boost only that perm lane rather than paying for full VT box.
  - Candidate synergy: Stable compound top `259` aligns with VTRAC’s top straights and DR’s candidate digit clusters (59x) — good for non-winner “environment describing” features in 2B.
- Q10:
  - Stable outputs are rich enough for Part 2 without raw CSV pasting: the summary already captures ranks + why-tags + hit flags. This is the exact workflow we want for future sessions.

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

## Top candidates (analyzer_v2_top_candidates.csv)
- rank 1 | variant Combined | best_pattern 599 | score_v2 16.287143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 2 | variant Combined | best_pattern 559 | score_v2 14.827143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 3 | variant Evening | best_pattern 599 | score_v2 13.227143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 4 | variant Combined | best_pattern 599 | score_v2 12.687143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac
- rank 5 | variant Evening | best_pattern 592 | score_v2 11.927143 | tags exact,vtrac,drop_exact,drop_vtrac,family_exact,family_vtrac

```

Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):
- Q1:
  - Important framing: Digit Reduction’s winners artifacts are anchored by `*_winner_stamp.json` (SSOT). For this run:
    - Midday winner = 678 (canonical 678)
    - Evening winner = 517 (canonical 157)
    - Combined winner = 678 (canonical 678)
  - Winners evidence (any vs final):
    - Midday 678: `exact_any=108/112`, `vtrac_any=112/112`, but `exact_final=0`, `vtrac_final=0`.
    - Evening 517/157: `exact_any=0`, `vtrac_any=102/112`, `vt_boxed=112/112`.
  - Brain evidence: DR’s top candidates are 599/559/592 clusters; the literal winner triads (678/517) are not emitted as DR `best_pattern` candidates in this run.
- Q2:
  - The 4 hit criteria (exact/boxed triad + VT) do **not** map 1:1 to Digit Reduction because DR is not a triad predictor by itself; it’s a reducer/scorer that outputs digit-level and candidate-cluster signals.
  - What we *can* map cleanly:
    - VT-boxed / VT-straight flags exist in DR winners artifacts (`dr_win_vt_boxed`, `dr_win_vt_straight`) and can be used as a support signal for the triad-level tools.
- Q3:
  - Alignment status: OK.
    - `winner_stamp.json` counts match sums in `winner_flags.csv` (any) and `winner_hits.csv` (final). The earlier “mismatch” was interpreting `final_value` as the winner; it’s per-item output.
    - `scripts/tools/validate_dr_winners.py` now validates stamp ↔ flags ↔ hits consistency.
- Q4:
  - DR’s strongest candidate clusters for this run are concentrated around 59x / 599 / 559 / 592 (top candidates list). That indicates a very “digit-clustered” environment, even though the raw triad winners are 678/517.
- Q5:
  - Top candidates (triad-level) from `analyzer_v2_top_candidates.csv`: 599, 559, 592 (plus repeated 599 variants).
  - Top per-item long patterns include: 5994033667 (Midday) and 592240133 (Evening).
  - These are high-value for cross-tool synthesis because they overlap other tools’ “environment” candidates (VTRAC top straights includes 592/593/259; Stable compound has 259; Hot Zones has 367).
- Q6:
  - DR did not surface the literal winner triads (678 / 517) as top `best_pattern` candidates in this run.
  - What it *does* surface is useful: strong “any” evidence density (Midday `exact_any=108/112`) and very strong VT-box coverage for Evening’s canonical family (157) — but with `*_final` counts at 0, so treat DR as a gating/strength layer, not a standalone predictor.
- Q7:
  - (V) Data read/schema OK: Yes (brain outputs + analyzer_v2 outputs + winners overlays exist).
  - (V) Columns populated: Yes; “any vs final” semantics are now explicit (stamp JSON is SSOT; `final_*_match` can be 0 by design).
  - (V) Winners/overlay artifacts written: Yes (winner_overlay.html and map/stamp files exist).
- Q8:
  - Workflow fix (done): DR summarizer/validator now treat `*_winner_stamp.json` as SSOT and report any vs final totals without filtering by `final_value`.
  - Optional future improvement: produce a “triad filter” artifact that explicitly says how DR’s final digit/value should constrain triad candidates (so it becomes easier to plug into the superbrain).
- Q9:
  - Cross-tool synergy idea: use DR as a **gating / reduction layer**:
    - If DR is confident on final digit/value, intersect Stable/VTRAC/Hot Zones candidate triads with that constraint to reduce spend.
    - Use DR’s top candidates (599/559/592) as “environment descriptors” even when they don’t match the literal winners; then see if other tools also light up those same clusters (2B).
- Q10:
  - DR outputs are now structured enough for the master validation report without raw CSV pasting: stamp/flags/hits semantics + top candidates are captured with provenance in the summarizer block.

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
- Q1:
  - Winners (post-results) for this date/state are:
    - Midday 678 → boxed index 21 (see winners lens JSON/HTML).
    - Evening 517 → boxed index 7 (see winners lens JSON/HTML).
  - Brain evidence (enhanced analyzer ranking) does **not** rank those indices highly:
    - Index 21: rank 14/35, score 11.85.
    - Index 7: rank 21/35, score 8.26.
  - Even when the index rank is mid-pack, some *within-index* signals line up:
    - For index 21, top “index straights” include `362` (which is also the #1 persistence survivor in the winners lens stats for 678).
    - For index 7, top “index straights” include `256` (a legitimate index7 family member; winners lens also shows 256 as a secondary survivor behind 175).
- Q2:
  - Exact boxed / Exact straight: N/A (VTRAC analyzer is not an exact-triad scorer; it’s an index/straight-lane analyzer).
  - VT-boxed: Yes in principle (it outputs ranked boxed indices), but for this example the winning indices (21, 7) were not top-ranked.
  - VT-straight: “Top straights” exist in the brain output (932, 923, 293, 259, 193, 592, 593, 362, …). The winners (678/517) are not in that short list; however the presence of `362` (which is also a winners-lens survivor) suggests there *was* a plausible VT-straight-adjacent lane, just not the literal winner straight.
- Q3:
  - The winners lens and brain are consistent at the “environment descriptor” level (e.g., 362 is important in both), but inconsistent at the “winner index prioritization” level (winning indices are mid/low ranked).
  - Treat this as the core Part 2 takeaway: the tool is producing signals, but its ranking weights may not yet match the winner reality for this example.
- Q4:
  - The section summaries show hot=20/superhot=12 everywhere but consensus_col1/col2 are False, suggesting no single col1/col2 consensus lane is dominating the VTRAC analyzer’s view.
  - That aligns with Part A’s finding that winners show via tight perm lanes embedded in strings, not as literal top straights.
- Q5:
  - Top indices (highest score): 20, 23, 30, 27, 28, 10, 29, 24, 33, 18 (see summary block for scores/features).
  - Top straights: 932, 923, 293, 259, 193, 592, 593, 362, 963, 913.
  - Cross-tool relevance: 259/592/593 also show up as strong “environment digits” in Stable/DR/Hot Zones, even though they are not the literal winners.
- Q6:
  - Miss (ranking) hypothesis: the scoring appears to overweight broad “presence” features and underweight the kind of “tight perm-lane + family-gap” signal we saw in the winners lens (e.g., 517 showing only via 175; 678 via 867/687).
  - Another likely factor: the VTRAC analyzer’s top indices differ from the winners indices, which may indicate it’s modeling a different “lane” concept than the winners lens (boxed index vs v-code straights vs straight candidates). This is an architectural clarity item to carry forward.
- Q7:
  - (V) Data read/schema OK: Yes (summary generated; enhanced JSON present).
  - (V) Expected outputs present: Yes (brain ranking + winners lens references present).
  - (V) No missing files flagged by the run-report checklist.
- Q8:
  - Highest-value tuning direction (log-only): adjust ranking so that when an index has a dominant survivor pattern in the winners lens (e.g., 367/362 for index21; 175 for index7), that index is boosted upstream in the brain ranking.
  - Clarify contracts in future outputs: explicitly label whether a “straight” is (a) an index member, (b) a v-code straight lane member, or (c) a top-permutation straight candidate, to reduce confusion in Part 2 evaluation.
- Q9:
  - Aggregator hook: intersect VTRAC analyzer “top straights” with Hot Zones “top lanes” and Stable/DR environment candidates. Example: `362` is a VTRAC top straight and a winners-lens survivor; `367` is a winners-lens survivor and a Hot Zones top lane.
  - Practical play hypothesis to test later: when VTRAC analyzer doesn’t rank the winning index highly, but a specific survivor straight like `362` is dominant, treat that as a “lane anchor” and build a reduced candidate set around it (instead of only using index rank).
- Q10:
  - For this first master validation example, VTRAC analyzer feels like a strong **environment lens** but not yet a strong **winner index ranker**. Logging this clearly now is exactly why Part 2 exists.

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
- Q1:
  - Winner evidence vs brain outputs:
    - Midday winner 678 (canonical 678): present in `hot_zones_top_lanes.csv` but weakly ranked (best rank 92). Per-lane flags indicate straight + vt-straight lanes exist.
    - Evening winner 517 (canonical 157): present in `hot_zones_top_lanes.csv` but very weakly ranked (best rank 106). Per-lane flags indicate straight + vt-straight lanes exist.
  - The *strongest* Hot Zones brain candidates are not the literal winners; they’re high-scoring lanes like 227/277/267/127/578/334/146/226/367/122.
  - Important: triad `367` is in Hot Zones Top 10 and also the dominant survivor in the VTRAC winners lens for the 678/index21 environment — a strong cross-tool anchor.
- Q2:
  - Exact boxed / Exact straight: Hot Zones is not a direct “exact winner” scorer; it ranks lanes/triads. Treat exact criteria as N/A for this tool alone.
  - VT-boxed: Not a primary output of Hot Zones, but it does carry `vt_triad` and `vt_only_lane` tags, which can support VT reasoning.
  - VT-straight: Yes as a lane feature (`vt_straight` tag; per-lane has_vt_straight=True). For this example, it indicates the tool recognized vt-straight lanes, even though it did not rank the literal winners highly.
- Q3:
  - Winners artifacts vs brain outputs are internally consistent:
    - “winner_map file exists but triad_present=False” is expected if the winner map is a Top-N snapshot, not an exhaustive list.
    - The actual ranked list (`hot_zones_top_lanes.csv`) still contains the winners (just low-ranked), which is the more important check.
- Q4:
  - The Hot Zones view is “busy”: many high-scoring lanes cluster around 2xx/3xx/5xx families (top 10 list), while winners (678/157) are far down the ranking.
  - This suggests Hot Zones is primarily surfacing “high-pressure lanes” rather than directly surfacing the next literal winner.
- Q5:
  - Top candidate lanes (Top 10): 227, 277, 267, 127, 578, 334, 146, 226, **367**, 122.
  - Cross-tool relevance: `367` is the standout because it is both:
    - A VTRAC winners-lens dominant survivor for index21 (678 environment), and
    - A high-scoring Hot Zones lane (rank 9).
- Q6:
  - Miss analysis: Hot Zones did not strongly prioritize the literal winners (678/157), which likely means:
    - Either the winner lane is not a “hot zone lane” by its criteria on this day, or
    - The Hot Zones scoring needs an explicit “if this lane is a dominant VTRAC family survivor, boost it” integration (log as aggregator hypothesis, not a code change yet).
- Q7:
  - (V) Data read/schema OK: Yes (per_lane/top_lanes/meta present; summary generated).
  - (V) Winner map present: Yes (but Top-N; not exhaustive).
  - (V) No missing artifacts flagged by the run checklist.
- Q8:
  - Optimization note (log-only): make the winner map either exhaustive or clearly labeled Top-N in the report (we already improved wording in the summary to distinguish file_present vs triad_present).
  - Aggregator-level improvement to test later: boost lanes that are both “hot zone strong” *and* “VTRAC family survivor strong” (e.g., 367).
- Q9:
  - Cross-tool seed:
    - Use Hot Zones to surface a small set of “lane candidates” (Top 10–20).
    - Intersect those with VTRAC winners-lens dominant survivors (e.g., 367/362/175 lanes) and Stable “coverage/why-tag” evidence to produce a reduced play set.
- Q10:
  - Hot Zones appears most valuable as a **lane ranking + feature tagger** (col1 funnels, verticals, vt_straight, etc.), not as a standalone winner predictor. That fits the superbrain direction: Hot Zones contributes “where pressure is,” while other tools contribute “which family/winner lane is live.”

---

## 2B — Cross-tool synthesis (after all tools)
- Shared clusters/signals:
  - Strong “environment anchors” show up repeatedly across tools even when they aren’t the literal winners:
    - `367` is the standout: it is the #1 occurrence survivor in the VTRAC winners lens for 678/index21 *and* it is a Hot Zones Top-10 lane (rank 9).
    - `362` is also key: it is the #1 persistence survivor in the VTRAC winners lens for 678/index21 and appears in the VTRAC analyzer brain’s Top straights list.
    - A 59x cluster shows up across DR + VTRAC brain + Stable: DR top candidates include 599/559/592; VTRAC brain top straights include 592/593/259; Stable compound includes 259 and 59. This looks like a recurring “pressure environment” signature even if it didn’t directly become the winner.
  - Part A’s main shared signal: both winners manifest through **tight permutation lanes embedded in longer strings**, not as literal winners sitting cleanly in the tables (678 via 867/687; 517 via 175 only).
- Conflicts/noise:
  - VTRAC analyzer brain ranking did not prioritize the winning boxed indices (21 and 7 were mid/low ranked). This is the biggest “brain vs reality” gap for this example.
  - Stable flagged exact_boxed/exact_straight for both winners, but the ranked score placement was mediocre (678) to very low (157). So: it can see winners but doesn’t elevate them.
  - Hot Zones ranked both winners very low (92/106 best ranks), even though it surfaced 367 strongly.
  - Digit Reduction winners artifacts show a likely semantic/logging mismatch between `winner_flags.csv` and `winner_hits.csv` (match_types populated but final_*_match sums are 0), making “hit auditing” ambiguous unless clarified.
- Aggregator/aux hooks to test next:
  - Perm-lane strategy (cheapness lever): when Part A shows only 1–2 permutations are present in-table (e.g., 517→only 175; 678→mostly 867/687), test an aggregator rule that prefers “play the in-table perm lane” over “play the full VT box,” unless other tools/aux indicate high uncertainty.
  - Intersection strategy (signal stacking): build a candidate set from intersections like:
    - Hot Zones Top lanes ∩ VTRAC winners-lens dominant survivors (e.g., 367/362 lane), then require Stable to provide “coverage evidence” (exact/vt_boxed flags) before promoting.
  - DR gating: treat DR as a digit/value constraint (not a triad predictor) and test whether applying it as a filter reduces candidate space without killing hit-rate.
  - Part 3 prep: use Aux compound scoring to explain *why* a tight perm lane was live (doubles pressure, positional pressure, repeat indices, etc.) and to decide when to trust “perm-only” vs “full VT” coverage.

---

## Part 3 — Aux Features (environment + compound evidence)

Primary evidence dump (generated from draw CSV snapshot):
- `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/summary.md`
- `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/summary.json`

### 3.Aux — OntarioCanada4 — 2025-06-21
0) Outputs reviewed
- Draw CSV snapshot (sharepack-stable): `sharepacks/2025-06-21/OntarioCanada4/aux/draws/` (Ontario_draws.csv, Ontario_Midday_draws.csv, Ontario_Evening_draws.csv)
- Aux evidence dump (sharepack-stable): `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/summary.md`
- Aux structured data: `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/summary.json`

Aux evidence dump:
- `sharepacks/2025-06-21/OntarioCanada4/aux/OntarioCanada4/summary.md` (already labeled by source; copy/paste here only if you need a single-file share)

1) Aux input validation (V)
- Snapshot mode: `generated_from_excel` from `data/history/Pick3StatsC4_2025_06_20.xlsm` (Aux state label: `Ontario`).
- Snapshot counts (max_n=1000):
  - Combined: `Ontario_draws.csv` n=1000 head=343, 211, 367, 221, 875
  - Midday: `Ontario_Midday_draws.csv` n=1000 head=211, 221, 847, 805, 890
  - Evening: `Ontario_Evening_draws.csv` n=1000 head=343, 367, 875, 896, 807
- Cross-check vs string-table “world snapshot” (Set1 Draw1 `draw_data`, columns 1–5):
  - Combined table (`sharepacks/2025-06-21/OntarioCanada4/tables/Combined_Combined.csv`): 343, 211, 367, 221, 875 ✅
  - Midday table (`sharepacks/2025-06-21/OntarioCanada4/tables/Midday_Combined.csv`): 211, 221, 847, 805, 890 ✅
  - Evening table (`sharepacks/2025-06-21/OntarioCanada4/tables/Evening_Combined.csv`): 343, 367, 875, 896, 807 ✅

2) Positional pressure (core)
- Variant top digits (rank 1):
  - Combined: P1=9 (gap=23), P2=8 (gap=28), P3=2 (gap=34)
  - Midday: P1=6 (gap=22), P2=7 (gap=28), P3=6 (gap=24)
  - Evening: P1=5 (gap=27), P2=3 (gap=28), P3=9 (gap=23)
- Hard-due positional digits: none (all variants).
- Winner overlap:
  - Midday winner `678`: matches Midday P1=6 and P2=7 (two direct positional hits), but not P3 top digit.
  - Evening winner `517`: matches Evening P1=5 (one direct positional hit), but not P2/P3 top digits.
- Notable higher-level positional signal: “Double-Pressure” and “Mirror-Echo” themes are present across variants (e.g., 0↔5, 1↔6, 2↔7, 3↔8, 4↔9). Both winners use digits inside these mirrored pressure clusters (678 uses 6/7/8; 517 uses 5/1/7), suggesting positional pressure is better treated as a **compound digit-level booster** rather than a direct 3-digit selector.

3) Positional shortlist (prediction list)
- Top shortlist candidates (from positional tool): 952, 959, 982, 989, 932, 752, 954, 939, 782, 732 (tags commonly include Double-Pressure + Mirror-Echo + XVAR consensus).
- Direct overlap with winners:
  - Midday winner `678`: not present.
  - Evening winner `517`: not present.
- Overlap with Part 2 “anchor” candidates (e.g., 367/362/175/599/592/227): none. This is an important observation: the positional tool is flagging a different “pressure lane” (9/5/2/8 style digits) than the string-tools’ strongest survivor families for this date/state.

4) Repeat-watch + index streak context
- Repeat-watch current index / streak:
  - Combined: current_index=33 streak=1 (max=3)
  - Midday: current_index=17 streak=1 (max=2)
  - Evening: current_index=33 streak=1 (max=3)
- Winner indices:
  - `678` → VTRAC index 21
  - `517` → VTRAC index 7
- Assessment: repeat-watch does not directly support either winner index here (it’s tracking different current indices). Treat repeat-watch as a **separate alert channel** (good for environment notes), not a primary winner booster for this example.

5) VTRAC overlay / heatboard (index pressure)
- Top overdue indices (draws since) per variant:
  - Combined: 32:687, 1:283, 6:115, 26:114, 13:108, 5:80, 16:64, 34:58, 28:57, 3:41
  - Midday: 32:343, 21:189, 16:185, 1:141, 34:126, 27:102, 26:89, 10:71, 33:62, 13:59
  - Evening: 32:674, 35:232, 6:195, 28:167, 1:147, 20:117, 3:114, 17:100, 26:57, 13:54
- Cross-variant pressure anchors:
  - Index 32 is *extremely* overdue across all 3 variants (Combined 687 / Midday 343 / Evening 674). Index 1 / 13 / 26 also recur in multiple variants.
- Winner index alignment:
  - Midday winner `678` (idx21): **strong** Midday support (idx21 ds=189 and in Midday top-overdue list) but not a cross-variant index anchor (Combined idx21 ds=2, Evening idx21 ds=1).
  - Evening winner `517` (idx7): **not** in top-overdue lists; low/normal ds values (Combined 12 / Midday 22 / Evening 6).
- Interpretation: for this example, index pressure helps explain the Midday win (idx21 lane is highly pressured in Midday), while Evening win did not come from “index due.” This reinforces “Aux is compound evidence, not a deterministic predictor.”

6) Doubles + pairs pressure
- Doubles: no direct winner alignment (both winners are non-doubles). Keep doubles as environment-level pressure (esp. multi-variant doubles alerts like 228/255/288/338/388/778).
- Pairs (winner-aligned):
  - Midday: `678` contains pair `67`, flagged as a pending non-repeating pair (ds=44, sev=blue).
  - Midday: `517` contains pairs `17` and `57`, both pending non-repeating pairs (ds=46/44, sev=blue).
  - Evening: `517` contains pair `15`, pending non-repeating pair (ds=25, sev=purple).
- Cross-variant pair alerts exist (see summary), but the key takeaway here is that **pair pressure did align cleanly** with both winners (especially via Midday’s blue non-repeating pair set).

7) Sums / root-sum pressure
- Winner sums:
  - Midday winner `678` sum=21: **strongly due** across all variants (draws_since=100; flags red+purple in Combined/Midday/Evening).
  - Evening winner `517` sum=13: not “due”, but **hot** in Evening (draws_since=9; flags blue=True).
- Interpretation:
  - Sum21 looks like an environment-level “deficit anchor” (very valuable compound feature for the day).
  - Evening sum13 looks like a localized “hot sum” (candidate-level booster), not a due anchor.

8) Blackapple (if enabled)
- Scores/triggers are present (Combined score=1; Midday score=2; Evening score=1), but:
  - The winners (678 / 517) are not in the top BA candidate lists for any variant.
  - The most relevant BA overlap is indirect: Midday shows root_due=[6] and floating digits include 6 (winner 678 contains 6), but this does not translate into direct BA candidate agreement.
- Conclusion: treat BA as “weak/neutral agreement” for this example; do not weight it heavily in Part 3 convergence for OntarioCanada4 on this date.

9) Aux convergence score (new, high-value)
Legend (signals per variant):
- `pos`: candidate appears in positional shortlist (positional tool)
- `idxTop`: candidate’s VTRAC index is in the variant’s top-overdue overlay list
- `sum`: candidate sum has a strong flag (red or blue)
- `pair`: candidate contains at least one pending pair (red/blue/purple) in the variant’s pair lists

Aux convergence table (winner + cross-tool anchors):
| triad | idx | sum | variants_supported | signals_total | C | M | E |
|---|---:|---:|---:|---:|---|---|---|
| 678 | 21 | 21 | 3 | 5 | sum | idxTop,sum,pair | sum |
| 517 | 7 | 13 | 2 | 3 | - | pair | sum,pair |
| 175 | 7 | 13 | 2 | 3 | - | pair | sum,pair |
| 367 | 21 | 16 | 1 | 2 | - | idxTop,pair | - |
| 362 | 21 | 11 | 3 | 4 | pair | idxTop,pair | pair |
| 599 | 15 | 23 | 3 | 4 | sum,pair | pair | pair |
| 592 | 12 | 16 | 3 | 3 | pair | pair | pair |
| 227 | 26 | 11 | 3 | 6 | idxTop,pair | idxTop,pair | idxTop,pair |
| 952 | 12 | 16 | 3 | 6 | pos,pair | pos,pair | pos,pair |
| 989 | 34 | 26 | 3 | 5 | pos,idxTop | pos,idxTop | pos |

Highlights:
- **Winner 678** has the cleanest “variant-correct” compound story: Midday idx21 pressure + Midday pending pair67 + sum21 deficit anchor across all variants.
- **Winner 517** is moderate-confidence: supported by pair pressure (Midday+Evening) and Evening’s hot sum13.
- **227 / 952 / 989** look “Aux-strong” but did not win → this is exactly why Aux must remain a *compound booster*, not the primary selector.

10) How to apply Aux (design implications + expense lever)
- Best use pattern (based on this example):
  - State-level gating: treat strong cross-variant anchors (e.g., sum21 deficit + index32 mega-due) as “playable environment” evidence.
  - Candidate-level boosts: within the Part 2 candidate set, boost candidates that stack multiple signals in the **correct variant** (e.g., 678 in Midday: idxTop + sum + pair).
- Expense lever (cheap play mode):
  - When Part 1 shows “tight perm lanes” and Aux strongly supports the winner lane, prefer **perm-only / in-table perms** over “play full VT-box”, unless uncertainty remains high across tools.
  - For this example, the strongest “cheap justification” is Midday 678: Aux is highly supportive in Midday; Part 1 noted the winner manifested via a tight perm lane (867/687). That’s the kind of scenario where an aggregator could recommend “play the in-table perms (+ optionally the literal if covered)” instead of full index coverage.
- Caution: the strongest *cross-variant* index anchor here is index32, but the winners are not index32. So: treat cross-variant index pressure as environment context, not an automatic candidate selector.

---

## Part 4 — Combination / Permutation Translation (Candidate Universe + Coverage Pack)

Goal: translate Parts 1–3 into a small “candidate universe” per draw + a concrete coverage pack decision (perm-only vs boxed vs VTRAC-straight vs full index-box). Evidence-first; no ROI/progression.

0) Inputs reviewed
- Part A (perm-lane notes): Midday winner 678 manifests mainly via in-table perms 687/867; Evening winner 517 manifests mainly via in-table perm 175 (canonical 157).
- Part 2B (cross-tool anchors): 367/362 dominant survivors for idx21; 59x cluster (599/592/259) is a strong environment signature; Hot Zones Top-10 includes 367 and 227.
- Part 3.9 (Aux convergence): strongest variant-correct support is 678 (idxTop in Midday + sum21 + pair67) and moderate support for 517/175 (pair + Evening hot sum13).
- VTRAC mapping ref: `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD` (Index members + permutations + VSTRAIGHTS).

### 4.1 Candidate universe (per draw)

Midday (targeting 678 / canonical 678):
- 678 (idx21): winner; strongest variant-correct Aux stack (Midday idxTop + sum21 + pair67); Part A shows tight perm lane around 678-family.
- 367 (idx21): dominant survivor (Part A); Hot Zones Top-10 lane rank 9; Aux supports via idxTop/pair (Midday).
- 362 (idx21): dominant persistence survivor (Part A); VTRAC brain “top straights” includes 362; Aux supports via idxTop/pair across variants.
- 268 (idx21): member of idx21 canonical set; useful as “index-box expansion” if we escalate from boxed to index coverage.
- 227 (idx26 double): Hot Zones #1 lane + very Aux-strong across variants (idxTop+pair everywhere), but *not* winner → keep as “false-positive anchor” to learn from (should not automatically override strings).
- 592 (idx12): cross-tool environment anchor (DR top candidates + VTRAC straights list); Aux supports via pair across variants (but did not win).

Evening (targeting 517 / canonical 157):
- 157 (idx7): canonical winner family; Stable flags it (exact boxed/straight), Hot Zones contains it (low rank), Aux supports via pair + Evening hot sum13.
- 175 (idx7): the main in-table permutation for the 157 family (Part A); boxing it covers 517; Aux support mirrors 517 (pair + Evening hot sum13).
- 567 (idx7): idx7 member; appears in v-straight lane v123 with 517; useful as “VT-straight lane expansion” if we play v123.
- 067 / 125 / 256 / 012 / 017 / 026 (idx7 members): only relevant if we escalate from boxed to full idx7 coverage (not recommended here).

### 4.2 Evidence vectors (compact)

Evidence vector legend (first-pass):
- Tools: `S`=Stable, `DR`=Digit Reduction, `VT`=VTRAC Analyzer, `HZ`=Hot Zones, `WL`=Winners Lens (HTML/JSON)
- Aux signals: `pos`, `idxTop`, `sum`, `pair`, `BA` (per Part 3.9)

Midday candidates:
| triad | canonical | idx | vstraight (example) | tools evidence | aux signals (C/M/E) | notes |
|---|---|---:|---|---|---|---|
| 678 | 678 | 21 | v234 contains 678 | WL=winner; S flags exact; HZ present (rank 92) | C=sum; M=idxTop,sum,pair; E=sum | strongest variant-correct Aux stack |
| 367 | 367 | 21 | v423 contains 367 | WL top-occurrence; HZ Top-10 rank 9 | C=-; M=idxTop,pair; E=- | cross-tool anchor (WL∩HZ) |
| 362 | 362 | 21 | v423 contains 362 | WL top-persistence; VT brain top-straight | C=pair; M=idxTop,pair; E=pair | persistent lane anchor |
| 268 | 268 | 21 | (idx21 member) | idx21 member (expansion only) | (not primary) | only for “index escalation” |
| 227 | 227 | 26 | v333 contains 227 | HZ #1 lane; Aux very strong | C=idxTop,pair; M=idxTop,pair; E=idxTop,pair | false-positive risk if overweighted |
| 592 | 592 | 12 | v153 contains 592 | DR top cluster; VT top straights list | C=pair; M=pair; E=pair | environment anchor (didn’t win) |

Evening candidates:
| triad | canonical | idx | vstraight (example) | tools evidence | aux signals (C/M/E) | notes |
|---|---|---:|---|---|---|---|
| 517 | 157 | 7 | v123 contains 517 | WL=winner; S flags exact; HZ present (rank 106) | C=-; M=pair; E=sum,pair | literal winner |
| 157 | 157 | 7 | (perm family) | canonical family (boxed covers 517) | C=-; M=pair; E=sum,pair | cheapest “safe” cover (boxed) |
| 175 | 157 | 7 | v231 contains 175 | Part A: main in-table perm lane; boxing hits 517 | C=-; M=pair; E=sum,pair | perm-lane anchor |
| 567 | 567 | 7 | v123 contains 567 | idx7 member; shares v123 with 517 | (not primary) | only if playing v123 lane |

### 4.3 Coverage mapping (counts + reference sets)

VTRAC index members (canonicals) from `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`:
- idx21: `123 128 137 178 236 268 367 678` (boxed index coverage ≈ 8×6=48)
- idx7: `012 017 026 067 125 157 256 567` (boxed index coverage ≈ 8×6=48)
- idx26 (double index): members listed as permutations (size differs; do not assume 48)

Coverage table (per key candidate):
| candidate | in-table perms observed (Part A) | exact boxed size | VT index boxed size | VT-straight lane size | recommended “cheap-safe” |
|---|---|---:|---:|---:|---|
| 678 (idx21) | {687, 867} (2) | 6 | 48 | 8 (v234) | Box 678 (6) |
| 367 (idx21) | (n/a) | 6 | 48 | 8 (v423) | Optional booster (straight/box) |
| 362 (idx21) | (n/a) | 6 | 48 | 8 (v423) | Optional booster (straight/box) |
| 517 (canonical 157, idx7) | {175} (1) | 6 | 48 | 8 (v123 covers 517) | Box 157 (6) |
| 175 (canonical 157, idx7) | {175} (1) | 6 | 48 | 8 (v231 covers 175) | Box 157 (6) |

### 4.4 Pack decision (no ROI)

Midday (targeting 678):
- Recommended “cheap-safe” pack: **Box 678** (6 combos).
- Optional add-ons (hypothesis testing only): add lane anchors `367`/`362` as 1-straights or 6-boxes *only* if you see multi-tool elevation in future examples.
- Why not full idx21 boxed? 48 is too heavy for this evidence level; we already have a strongly supported primary candidate.

Evening (targeting 517):
- Recommended “cheap-safe” pack: **Box 157** (6 combos) — covers literal 517 as a permutation.
- Why not perm-only? Part A shows the in-table perm lane as `175`, but the winner is `517`; perm-only would miss.
- Why not full idx7 boxed? 48 is too heavy given we have a strong canonical-family candidate.

Total “cheap-safe” across both draws (Ontario): 6 + 6 = **12 combos** (post-hoc: would have hit both as exact boxed).

### 4.5 Optional method checks (log-only)
- Not executed in this first run. Candidate methods to test later: `docs/AAT9_KIT/FINAL VALIDATION/combination_forming_2.txt` (12-combo method; consensus method).

---

## Part 5 — Overall Summary (Key Insights + Fix/Future Hooks)

### 5.1 Pack vs winners (post-hoc validation)
- Midday 678:
  - Exact boxed: ✅ (Box 678 hits)
  - Exact straight: ✅ only if 678 straight included (not required for boxed)
  - VT-boxed: ✅ if idx21 boxed played (not needed here)
  - VT-straight: ✅ if v234 lane played (not needed here)
- Evening 517 (canonical 157):
  - Exact boxed: ✅ (Box 157 hits)
  - Exact straight: ✅ only if 517 straight included (not required for boxed)
  - VT-boxed: ✅ if idx7 boxed played (not needed here)
  - VT-straight: ✅ if v123 lane played (not needed here)

### 5.2 Key environment tags
- High Set1 col1/col2 heat (macro “pressure”)
- Tight permutation-lane manifestation (winners show via a small perm subset in-table)
- Strong due-sum anchor (sum21 due across all variants)
- Variant-specific index pressure (idx21 is Midday-overdue; Evening win not “index due”)
- Pair-pressure alignment (67 / 15 / 17 / 57 pending)
- Mixed/noisy tool rankings (winners often present but not elevated)

### 5.3 What drove the wins (best evidence)
- Midday 678: Aux convergence story is clean and variant-correct (Midday idx21 overdue + pair67 pending + sum21 deficit anchor across variants).
- Evening 517: winner family (157) is supported by pair pressure + Evening hot sum13; Part A shows family present via perm lane 175 (boxed family capture is the safe play).
- Cross-tool anchor `367`: Hot Zones Top-10 ∩ Winners-lens dominant survivor suggests a usable “lane anchor” even when literal winner isn’t elevated.

### 5.4 Biggest conflicts / miss patterns
- VTRAC Analyzer brain ranked indices 20/23/30/27/28 highest; winning idx21/idx7 were not top-ranked → “brain vs reality” gap.
- Stable flags exact winners but doesn’t elevate them (678 mediocre; 157 very low) → “sees but underweights.”
- Hot Zones ranks both winners very low (92/106), but correctly surfaces 367 strongly → suggests Hot Zones is more “pressure lanes” than “literal next winner.”
- Digit Reduction top candidates cluster around 59x (599/559/592) and does not surface winner triads as candidates → treat DR as gating/constraints rather than a primary triad selector.

### 5.5 Fix-now vs fix-later
- Fix-now: none blocking repeatable master validation runs for Ontario on this date (all sharepack artifacts present; drift checks passed).
- Fix-later (aggregator hypotheses):
  - Combine Hot Zones Top lanes ∩ Winners-lens dominant survivors (e.g., 367) as a candidate reducer before spending.
  - Add a “dominant survivor boost” concept to VTRAC analyzer index ranking (log-only; do not change code yet).
  - Use DR as a digit/value constraint layer to reduce candidate space (not as a direct predictor).

### 5.6 Next run recommendation
- Run one more state (e.g., Connecticut4) for the same date to test whether:
  - “tight perm-lane manifestation” repeats, and
  - Aux convergence reliably points to the correct variant winner (vs producing strong false positives like 227/952/989).
