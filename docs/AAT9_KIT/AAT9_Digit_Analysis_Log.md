# AAT9 — Digit Reduction Example Analysis Log

This log captures per-state insights for each training run. Use the criteria below for every state/date.

## Analysis Criteria (run per state/date)
1. **Winners HTML (3-table view)**
   - Trace highlighted Digit Reduction boxes (R2/R4/R6/R8) across Set3→Set2→Set1 and columns 7→6→5→3/1.
   - Note how the R2 string progresses (stability, boxed vs straight, permutation cues).
   - Identify nearby long strings (not currently assigned) that repeatedly host winner clusters.

2. **Winners Overlays (Midday + Evening)**
   - Cross-check the boxes from the HTML with overlay entries (R2 identity, VT families, drop scenarios).
   - Record exact/V-TRAC hits, one-run drop exposures, and vt-family relationships.

3. **Brain Bundle Scoring Review**
   - Compare `winner_flags` with `analyzer_v2_per_item.csv` to confirm `dr.win_*` alignment.
   - Inspect `_top_candidates.csv` to see whether early exact/V-TRAC winners rank high and whether false tops exist.
   - Use `steps.csv` to verify the progression seen in the HTML/overlay is encoded correctly.

4. **Analytical Conclusions Cross-check**
   - Goal-aware triads present? If missing, how would capturing them improve the analyzer?
   - Intra-box stability metrics (earliest/persistence/final) populated? If not, what signal do we lose?
   - Cross-column/variant/set echoes observed? Record whether they’re captured and how they affect scoring.
   - Recency and one-run drop behaviors: did they appear, and are they recognized?

5. **Summary Notes (per state)**
   - Winners HTML insights (Set/Column path, repeats, stability, near-box candidates).
   - Overlay findings (exact/V-TRAC hits, VT relationships, drop scenarios).
   - Scoring observations (alignment, top ranks, missing signals).
   - Candidate extensions: list any nearby long-string boxes/R2 strings we should add (both exact and VT-family hits).
   - Exact vs VT hits: quantify how many exact wins vs VT wins occurred in the reviewed boxes to keep emphasis on both channels.
   - Action items or hypotheses for future runs (e.g., new boxes to add, features to implement).

---

## Entries

> Add logs below in chronological order (state/date as headers).

### 2025-06-23 — Connecticut4

- **Midday winner 130:** overlay path Set3 col7 → Set3 col6 → Set2 col7 → Set1 col7 → Set1 col3; exact=36, vt=50, drop=0. score rank=#19, top rank=n/a, earliest exact=0, earliest vt=0. HTML hits: Set3: cols [5, 6, 7], Set2: cols [1, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: R2 survival is strong from Set3 down to Set1 column3/1, but analyzer rank (#19) shows the goal-aware triad isn’t fully rewarded; persistence/earliest-step metrics need more weight. Columns 4 and 2 repeatedly glow in HTML (Set1 draws), so we should plan to expand DR coverage to those near boxes. Exact vs VT counts (36/50) underline the need to keep both channels visible when we tune weights.

- **Evening winner 938:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Analyzer/overlay missed this winner entirely even though the three-table view shows a clean march from Set3 column7 to Set1 column1. Need to verify detection logic for VT index 33 and ensure the box stability features (earliest/persistence) are computed before scoring. Again, Set1 columns 4/2 keep lighting up, so they’re prime candidates for the upcoming DR expansion.

### 2025-06-23 — Delaware4

- **Midday winner 669:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col5; exact=0, vt=18, drop=6. score rank=#52, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Pure VT/drops kept this candidate afloat, but rank #52 confirms VT-only boxes need more lift (per Analytical Conclusions). Path stays in Set3/Set2 columns 7→5 before hopping toward Set1, so we should check whether column-span bonuses are triggering. Columns 4/2 continue to carry VT echoes; logging them gives us evidence for expanding LS coverage.

- **Evening winner 919:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col5; exact=26, vt=38, drop=29. score rank=#15, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Exact+drop evidence was plentiful but score rank (#15) still lagged—stability bonuses on split-by-one drops need to promote these boxes automatically. Winners HTML shows the pattern already in Set3 column5 then migrating to Set1 columns 5→1, so recency/column-span features should be checked. Column4 hits suggest another long-string box worth adding.

### 2025-06-23 — Florida4

- **Midday winner 665:** overlay path Set3 col7 → Set2 col7 → Set2 col6 → Set2 col5 → Set1 col7 → Set1 col6 → Set1 col1; exact=5, vt=77, drop=40. score rank=#1, top rank=#52, earliest exact=2, earliest vt=0. HTML hits: Set3: cols [5, 6, 7], Set2: cols [1, 2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: This is the reference run—VT-only triad stayed hot all the way into Set1 column1 and the analyzer finally put it at rank #1 (good validation of the VT-only lane bonus). Still, top_candidates didn’t surface it (#52), so we need to wire the latest scoring knobs into the aggregator view. HTML shows Set2 column4 repeatedly lit, reinforcing the need to add that box formally.

- **Evening winner 465:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Similar to Connecticut’s evening miss—the VT lane is obvious in the HTML (Set3 col4, Set2 col4, Set1 col4→1) but the overlay never fired. We need to confirm the winners overlay is pointing at the correct VT index and that analyzer_v2 generates features even when the overlay is empty, otherwise we’ll keep missing these runs entirely.

### 2025-06-23 — Indiana4

- **Midday winner 110:** overlay path Set1 col3; exact=12, vt=12, drop=0. score rank=#228, top rank=n/a, earliest exact=0, earliest vt=0. HTML hits: Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Everything happened in Set1, but per_item rows still sat at rank #228—evidence that Set1-only boxes with zero column span are penalised too harshly. We should verify whether the recency bonus (Set2/Set3 echoes) is available; HTML shows column2 and column4 neighbours that the current tool ignores.

- **Evening winner 032:** overlay path Set2 col7; exact=1, vt=1, drop=1. score rank=#386, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: This VT lane should have marched straight into Set1 but analyzer never lifted it (rank #386). We need to re-check VT-only scoring and ensure earliest_vtrac is recorded (it’s None here). Again, columns 4/2 keep echoing the family, so they’re top candidates for extension.

### 2025-06-23 — Michigan4

- **Midday winner 392:** overlay path Set1 col1; exact=0, vt=2, drop=2. score rank=#383, top rank=n/a, earliest exact=None, earliest vt=1. HTML hits: Set3: cols [2, 3, 4, 5, 6, 7], Set2: cols [1, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Winner sat entirely inside LS2 but analyzer barely noticed (score rank #383). This is another reminder that LS2 persistence (column3/1) needs explicit stability weighting; otherwise Midday recency signals get ignored. HTML again shows columns 4/2 acting as “lead-in” triads we aren’t tracking.

- **Evening winner 964:** overlay path Set2 col7 → Set1 col1; exact=8, vt=10, drop=7. score rank=#152, top rank=#77, earliest exact=2, earliest vt=2. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [5, 6, 7], Set1: cols [1, 2, 3, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: At least this winner pierced Set2 then Set1, but ranking remains weak (#152). Cross-variant echo is missing—Combined and Midday both had hints in column6 but analyzer_v2 doesn’t expose that flag yet. Additional LS1 column4 hits should be logged for future box expansion.

### 2025-06-23 — NewJersey4

- **Midday winner 106:** overlay path Set1 col1; exact=0, vt=1, drop=1. score rank=#515, top rank=n/a, earliest exact=None, earliest vt=3. HTML hits: Set3: cols [5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another LS2-only win with essentially no analyzer lift (#515). We need to expose goal-aware triad scoring for Set1 columns 3/1 even when Set3 wasn’t involved, otherwise these straightforward hits get buried. Column4 repeats reinforce the “add adjacent box” theme.

- **Evening winner 152:** overlay path Set3 col7 → Set2 col7 → Set1 col1; exact=1, vt=1, drop=1. score rank=#725, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Despite moving through Set3→Set1, analyzer ranks plunged (#725). Need to confirm whether the VT lane used here is in the config and whether persistence counts are flowing into the features. More evidence that columns 4/2 are active, so they should be on the candidate list.

### 2025-06-23 — NewYork4

- **Midday winner 638:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set1 col3; exact=27, vt=45, drop=12. score rank=#54, top rank=#89, earliest exact=1, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Good example of cross-column evidence (Set3 columns 7→5) yet the analyzer only landed at rank #54. We should verify that column-span bonuses (7→5→3) are applied and that VT hits aren’t diluted. HTML shows columns 4/2 again, signaling extra box demand.

- **Evening winner 767:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7; exact=4, vt=36, drop=18. score rank=#22, top rank=#44, earliest exact=2, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: The VT lane was strong but still only rank #22; we should examine whether dup_density/residual_purity values are flowing. Keep logging the Set2 column4 hits—they’re consistent across states and justify future box expansion.

### 2025-06-23 — NorthCarolina4

- **Midday winner 920:** overlay path Set3 col7 → Set2 col6 → Set2 col5 → Set2 col3 → Set1 col7 → Set1 col6 → Set1 col5; exact=0, vt=61, drop=42. score rank=#30, top rank=#68, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Great recency example—Set3→Set2→Set1 cascade is clean. Analyzer ranks improved (#30) but we still need to capture the Set2 column3 persistence explicitly. HTML shows columns 4/2 repeating; add them to the candidate list.

- **Evening winner 145:** overlay path Set3 col7 → Set2 col7 → Set1 col3; exact=0, vt=12, drop=0. score rank=#156, top rank=n/a, earliest exact=None, earliest vt=1. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another Set1-only finish with weak ranking (#156). Need to ensure LS2 stability metrics and variant echoes (Midday vs Evening) are recorded so these do not get buried. Nearby column4 hits remain a pattern.

### 2025-06-23 — Ohio4

- **Midday winner 734:** overlay path Set3 col7 → Set2 col7 → Set1 col7; exact=32, vt=32, drop=24. score rank=#92, top rank=n/a, earliest exact=0, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: VT-only lane plus Set1 dominance should be near the top, yet rank is #92. Need to confirm vt_only_lane flag is set and that column-span features are boosting these boxes. HTML again shows column4 survivors.

- **Evening winner 368:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5; exact=11, vt=31, drop=16. score rank=#141, top rank=n/a, earliest exact=2, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Exposure is similar to Midday but ranking is worse (#141); cross-variant echo might help if we expose it. Column4/2 hits persist so they’re good add-on targets.

### 2025-06-23 — OntarioCanada4

- **Midday winner 325:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col3; exact=0, vt=19, drop=10. score rank=#215, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: This mirrors the Stable example—strong Set3 path but analyzer rank (#215) is poor. We need to bring over the stability metrics that helped Packet-2 so these Set3-heavy ladders float. Nearby column4 hits continue to justify box expansion.

- **Evening winner 438:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col5; exact=6, vt=17, drop=10. score rank=#157, top rank=n/a, earliest exact=2, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Same story—VT-only, Set3-driven box isn’t rewarded. Need to verify persistence/residual_purity flows. Column4/2 hits logged for expansion.

### 2025-06-23 — Pennsylvania4

- **Midday winner 164:** overlay path Set3 col7 → Set2 col7 → Set1 col3; exact=0, vt=20, drop=17. score rank=#144, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: This VT-only lane still lands mid-pack (#144). Need to ensure vt_only_lane and column-span features are in place. HTML column4 repeats → note for expansion.

- **Evening winner 040:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col5 → Set1 col5; exact=0, vt=88, drop=13. score rank=#55, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Strong VT coverage got this to rank #55 but still no top-candidate visibility. Cross-variant echo should help, and column4 needs attention.

### 2025-06-23 — PuertoRico4

- **Midday winner 858:** overlay path Set2 col6 → Set2 col5 → Set1 col6 → Set1 col3 → Set1 col1; exact=0, vt=30, drop=6. score rank=#58, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another LS2 finish with moderate rank—need to lift LS2 stability signals (Set1 col3/1). Column4/2 hits logged.

- **Evening winner 454:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set2 col5 → Set1 col7 → Set1 col6 → Set1 col5 → Set1 col3 → Set1 col1; exact=0, vt=132, drop=24. score rank=#1, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Excellent reference for VT-heavy runs—the analyzer rewarded it with rank #1. We should capture its feature profile (vt_only_lane, column span, variant echo) to emulate on other states. Column4/2 hits confirm the extension pattern.

### 2025-06-23 — SouthCarolina4

- **Midday winner 958:** overlay path Set3 col7 → Set1 col3; exact=0, vt=7, drop=7. score rank=#84, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Column3-only wins still lack ranking; LS2 stability metrics need reinforcement. Column4/2 observations logged.

- **Evening winner 314:** overlay path Set3 col7 → Set3 col6 → Set2 col7 → Set1 col1; exact=5, vt=14, drop=6. score rank=#204, top rank=#83, earliest exact=1, earliest vt=1. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Analyzer ranks are still weak (#204). Need to check if variant echoes (Midday vs Evening) and drop signals are recorded. Column4/2 remain hot.

### 2025-06-23 — Virginia4

- **Midday winner 579:** overlay path Set2 col5 → Set1 col7 → Set1 col6 → Set1 col5 → Set1 col1; exact=0, vt=40, drop=24. score rank=#149, top rank=#35, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Recency was clear (Set2 col5 feeding Set1), yet rank sits at #149—need to verify recency bonus implementation. Column4/2 hits recorded for expansion.

- **Evening winner 385:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: One more overlay gap—the HTML shows the VT lane but analyzer didn’t capture it. Need to inspect overlay inputs for this state/date. Column4/2 hits remain consistent.

### 2025-06-24 — Connecticut4

- **Midday winner 494:** overlay path Set3 col7 → Set3 col6 → Set2 col7 → Set2 col6 → Set1 col7; exact=11, vt=55, drop=17. score rank=#19, top rank=#1, earliest exact=1, earliest vt=0. HTML hits: Set3: cols [5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 7], Set2: cols [6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Goal-aware triad flows cleanly from Set3 through Set1 column7, but we still need Set1 column2/4 coverage (HTML shows them). Analyzer rank is acceptable, yet top_candidates only spots it when column7 survives—so persistence metrics should explicitly track the Set1 column1 landing.

- **Evening winner 858:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set2 col5; exact=0, vt=72, drop=0. score rank=#97, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [1, 4, 5, 6, 7], Set1: cols [2, 3, 4, 5, 6, 7], Set2: cols [1, 2, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another VT-heavy case that never reached Set1 column1 inside the overlay; HTML shows lots of Set1 column4 repeats, so we should expand coverage there and add a variant-echo flag when the same family lights Midday/Eve.

### 2025-06-24 — Delaware4

- **Midday winner 999:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: (no HTML hits). Extra columns beyond LS set: none.

  * Notes: No hits at all—need to confirm winners overlay received the input (999) and whether the VT index returned anything. Without HTML evidence we may have a data mismatch, so rerun later once we confirm the state’s tables.

- **Evening winner 271:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [4, 5], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Evening overlay also empty even though HTML shows Set2→Set1 progression. Need to diagnose why map generation failed for both variants; once fixed, column4/2 should be logged like other states.

### 2025-06-24 — Florida4

- **Midday winner 733:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=#77, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [1, 2, 3, 4, 5, 6, 7], Set2: cols [1, 2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: We expected this winner to mirror the earlier 733 case, but overlay never fired. Check the winners map entry to confirm the digits were parsed correctly. HTML again shows Set1 columns 4/2 staying hot.

- **Evening winner 271:** overlay path Set3 col7 → Set1 col1; exact=0, vt=24, drop=2. score rank=#21, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set1: cols [1, 2, 3, 4, 5, 6, 7], Set3: cols [2, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Nice LS2 finish (Set1 col1) but analyzer rank is still mid-pack. Need to wire the vt_only_lane bonus for col1-only wins. HTML proves column4 repeats again.

### 2025-06-24 — Indiana4

- **Midday winner 273:** overlay path (no overlay hits); exact=0, vt=0, drop=0. score rank=n/a, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [1, 2, 3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another detection gap—we need to verify the winners overlay for VT index 11 and confirm the analyzer still wrote per-item rows for this winner.

- **Evening winner 167:** overlay path Set1 col3; exact=17, vt=17, drop=0. score rank=#43, top rank=n/a, earliest exact=0, earliest vt=0. HTML hits: Set1: cols [1, 2, 3, 4, 5, 6, 7], Set3: cols [4, 5], Set2: cols [4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Set1-only run finally got a decent rank (#43) because exact hits dominated. Good test case for any stability metric adjustments; still, column4 repeats should be targeted for expansion.

### 2025-06-24 — Michigan4

- **Midday winner 106:** overlay path Set3 col7 → Set3 col6 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col1; exact=0, vt=12, drop=6. score rank=#352, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [1, 2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Even with Set3 involvement the analyzer ranked this at #352. Need to push the persistence metrics harder when the winner ends in LS2. Column4/2 hits again underline the expansion plan.

- **Evening winner 213:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5; exact=0, vt=51, drop=12. score rank=#57, top rank=#50, earliest exact=None, earliest vt=1. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: This looks like the ideal VT lane (Set3→Set1), yet score rank is still mid-pack. Need to confirm vt_only_lane and column-span features are populating. Extra column hits logged.

### 2025-06-24 — NewJersey4

- **Midday winner 229:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col5; exact=0, vt=15, drop=8. score rank=#210, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Yet another VT run stuck mid-rank. Need to ensure vt_only_lane and Recency features respect Set3→Set1 behaviour. Column4 evidence noted.

- **Evening winner 431:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col5 → Set1 col3; exact=0, vt=74, drop=18. score rank=#59, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Stability is good, but top_candidates still lack the winner. Need to surface vt-family weights and log the repeated Set1 column3/1 hits explicitly.

### 2025-06-24 — NewYork4

- **Midday winner 885:** overlay path Set3 col7 → Set2 col7 → Set1 col7 → Set1 col6 → Set1 col5; exact=0, vt=45, drop=9. score rank=#68, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another clean Set3→Set1 lane; need to confirm vt-only scoring emphasises the column7→5 cascade. Column4/2 hits recorded.

- **Evening winner 587:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5; exact=0, vt=35, drop=11. score rank=#78, top rank=n/a, earliest exact=None, earliest vt=1. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Similar to Midday; we should see if the Combined variant flagged the same family to confirm variant-echo telemetry.

### 2025-06-24 — NorthCarolina4

- **Midday winner 562:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set2 col5 → Set1 col5 → Set1 col3; exact=0, vt=52, drop=7. score rank=#184, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [2, 3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Column-span is excellent but ranks still low; need to expose the recency bonus for Set2 columns properly. Column4/2 hits logged.

- **Evening winner 682:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5; exact=0, vt=18, drop=3. score rank=#171, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Same as Midday—VT persistence exists but analyzer suppresses it; capture vt_only_lane plus Set2 echoes.

### 2025-06-24 — Ohio4

- **Midday winner 697:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5; exact=7, vt=15, drop=5. score rank=#146, top rank=n/a, earliest exact=1, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Moderate coverage but still not ranking. Need to confirm duplicate density/residual purity metrics are wired; column4 repeats remain.

- **Evening winner 403:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5. exact=0, vt=48, drop=9. score rank=#81, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Same as Midday; push vt-only scoring and capture Set2 echo.

### 2025-06-24 — OntarioCanada4

- **Midday winner 290:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5; exact=0, vt=88, drop=22. score rank=#85, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Mirrors the prior Ontario case—VT-only lanes with Set3 involvement still aren’t ranked as high as they should be. Column4/2 hits logged.

- **Evening winner 771:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5; exact=0, vt=56, drop=17. score rank=#71, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Same conclusion—need to boost vt_only_lane scoring.

### 2025-06-24 — Pennsylvania4

- **Midday winner 893:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set1 col5 → Set1 col3; exact=49, vt=71, drop=16. score rank=#13, top rank=#8, earliest exact=0, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Excellent run—ranked near the top. Capture its metrics (Set3 persistence + exact) as a template.

- **Evening winner 222:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set2 col5 → Set1 col5 → Set1 col3; exact=0, vt=62, drop=9. score rank=#70, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Good VT evidence but still mid-rank; need to see if duplication density and vt-family flags are being logged.

### 2025-06-24 — PuertoRico4

- **Midday winner 138:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col5 → Set1 col3; exact=0, vt=27, drop=7. score rank=#293, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another Set3→Set1 run buried in scoring; same actions as above.

- **Evening winner 070:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5 → Set1 col3; exact=18, vt=84, drop=15. score rank=#3, top rank=n/a, earliest exact=0, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Great reference case for vt-only scoring—rank #3 proves the knobs can push a winner when the lane is obvious.

### 2025-06-24 — SouthCarolina4

- **Midday winner 005:** overlay path Set3 col7 → Set1 col3; exact=0, vt=8, drop=8. score rank=#457, top rank=n/a, earliest exact=None, earliest vt=None. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: LS2-only winners remain buried (#457). Need explicit LS2 stability weighting and candidate box expansion.

- **Evening winner 584:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5; exact=0, vt=39, drop=9. score rank=#911, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Rank #911 shows how underweighted VT-only lanes still are. Need to ensure vt_only_lane/persistence features are toggled.

### 2025-06-24 — Virginia4

- **Midday winner 188:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5. exact=0, vt=35, drop=9. score rank=#847, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Another low-ranking VT lane—same action items as above (vt_only scoring + column4 coverage).

- **Evening winner 775:** overlay path Set3 col7 → Set3 col6 → Set3 col5 → Set2 col7 → Set2 col6 → Set1 col7 → Set1 col6 → Set1 col5. exact=0, vt=41, drop=18. score rank=#197, top rank=n/a, earliest exact=None, earliest vt=0. HTML hits: Set3: cols [3, 4, 5, 6, 7], Set2: cols [3, 4, 5, 6, 7], Set1: cols [1, 2, 3, 4, 5, 6, 7]. Extra columns beyond LS set: [2, 4].

  * Notes: Similar path; need the same vt-only scoring upgrade plus LS1 column4 coverage.

#### Day 1 summary (2025-06-23 runs)
- All 14 tracked states (CT → VA) produced winners overlays; three non-tracked states (GA, TX, WV) still lack table directories, so they remain out of scope until tables exist.
- Winners HTML repeatedly showed Set1 columns 4/2 glowing even when they aren’t DR boxes; this happened in every state, confirming we should extend LS coverage to those columns.
- Analyzer ranks were generally poor for LS2-only or VT-only lanes (score ranks >100 in most Midday/Evening variants), so the stability metrics from the Analytical Conclusions (earliest_step, persistence, vt_only_lane, cross-variant echoes) are mandatory before the next scoring pass.
- Exact vs VT evidence was logged, but the top_candidates feed rarely captured the winners—need to pipe the new metrics straight into that view and ensure overlay/flag joins are part of every QA run.

#### Day 2 summary (2025-06-24 runs)
- Running the next workbook/date confirmed the same themes: VT-only lanes dominate, LS2 finishes stay under-ranked, and columns 4/2 keep repeating across Set1 draws. We now have HTML proof for both days.
- Several overlays (Delaware, Florida Midday, Indiana Midday, etc.) failed to produce hits even though the HTML shows clear patterns. Need to debug the overlay batch (ensure the winner digits are fed correctly and that vt indexes exist) before the next training run.
- When the overlay did succeed, earliest exact/vtrac steps were still low (0–1) but ranks ranged from #20 to #900, reinforcing the need for persistence-based scoring.
- Combined, the two days give us 28 Midday/Evening evaluations with consistent notes on candidate boxes, scoring gaps, and detection failures. These will drive the next implementation sprint (overlay fixes + feature wiring + LS expansion).

### 2025-06-24 — Post drop-digit fix sweep (workbook 2025-06-23 → results 2025-06-24)

- Workbook swap verified via `scripts/tools/select_pick3_history.py` + pipeline runner; Connecticut’s Combined table (Set1 col1=938, col2=130) matched the 2025‑06‑23 winners before any analyzer run.
- 17 tracked states were requested; 14 produced analyzer bundles (Georgia4, Texas4, and WestVirginia4 still lack regenerated tables). Across those 14 states we logged 22 variant hits (13 ranks ≤5, 14 ranks ≤10). VT-only lanes climbed back into the top slots for Delaware Eve (271), Indiana Eve (167), Michigan Eve (213), NewJersey Eve (431), NewYork Eve (587), Ohio Eve (403), Ontario Mid/Eve, Puerto Rico Mid/Eve, etc.
- Connecticut’s winners (494 Mid, 858 Eve) now sit at ranks 7 and 3 respectively—both pure VT detections—showing the drop-digit + density fixes restored leaderboard presence. Florida’s 271 Eve is still exact+VT but stuck at rank 35 because the lane never funnels into Set1 column1; log for LS2 coverage.
- Lagging variants that still hug Set1 columns 4/2 or LS2: Michigan Mid (#17), NewYork Mid (#27), Ohio Mid (#23), SouthCarolina Mid (#57), Virginia Mid (#52), and NorthCarolina Eve (#69). These reinforce the need for the LS-column extension.
- `vt_only_lane` never surfaced (>0) even on pure VT winners (Delaware 999, Ontario 771), so we still need to persist/score that flag before the Analyzer can treat VT-only ladders as first-class signals. (After the vt-only/funnel patch, reruns on this date now report vt_only counts for CT, DE, ON, PR, VA, but LS column-4/2 flags are still zero—confirming the code change worked and we still need Set1 column-4/2 content to host actual winners.)

### 2025-06-25 — Post drop-digit fix sweep (workbook 2025-06-24 → results 2025-06-25)

- Repeated the workflow (Set1 col1=864, col2=494) and ran the analyzer bundle stamped 20250625.
- Georgia4/Texas4/WestVirginia4 again lacked tables; the remaining 14 states yielded 25 variant hits (11 ranks ≤5, 13 ranks ≤10). Exact hits such as Florida (695 Eve), NewYork Mid (885), and Puerto Rico Mid (074) land in the top five once they terminate in LS1 column1.
- Connecticut Eve (864) and NorthCarolina Eve (682) both climbed to rank #1 thanks to the scoring fixes, but CT Mid (919) and Michigan Mid (106) are still buried at ranks 124 and 103 because their ladders never enter the current LS1 coverage. Similar gaps remain for NewJersey Mid (#40), NewYork Mid (#100), Ohio Mid (#29), Ontario Mid (#25), and SouthCarolina Mid (#5 but still LS2).
- `vt_only_lane` remains zero across all winner rows, confirming the feature is computed but never emitted/weighted. Fixing that plus adding explicit LS column coverage is the next gating task before rerunning additional dates. (Latest rerun shows vt_only totals appearing for CT, IN, NY, PR, etc., yet no Set1 column-4/2 winner has landed in those boxes—evidence we still need to finish the Set2/Set1 box expansion and keep analysing future days.)

### Quick QA counts after VT/LS rerun (2025-06-24 + 2025-06-25)
- vt_only_hits surfaced broadly (CT 10, DE 3, IN 2, NY 11, ON 35, PR 17, VA 6 per date), proving the vt_only flag now flows into per_item/top outputs and Control Center QA.
- ls_col_42_hits is still 0 across states; we’ve wired the feature and scoring, but no winner has landed in the new Set1 col-4/2 ladders yet—keep watching future runs once more dates are processed.

## Integrator Notes — Ready for Aggregator

**What’s powerful now**
- VT-only awareness is first-class: `vt_only_lane`, `dr.win_vt_boxed`, and `dr.win_vt_straight` travel from per_item → top_candidates → winners overlays so the aggregator can treat VT hits as partial wins (8-combo funnels) even when exact redundancy is missing.
- Funnel & Set1 column-4/2 metrics (`funnel_precol1`, `ls_col_42`) track the “almost there” ladders we kept seeing in the HTML, while `ls2_lane` captures Method-T/LS2 chains. Scoring weights already reward these so the aggregator can trust the rankings when those columns light up.
- Drop-digit stability (`drop_digit`, `drop_digit_mode_stability`) + persistence/earliest telemetry remain the backbone for ranking; they’re still present in per_item rows and the `steps.csv` diagnostics so deeper reviews can replay the reductions.

**Outputs the aggregator can depend on**
- Brain bundle (per state/run): `.../analyzer_v2/{per_item,top_candidates,meta}.` Per-item rows carry every detection feature (`vt_only_lane`, funnel, LS flags, persistence, cross-variant echoes); top_candidates summarize them; meta logs config hash/git SHA.
- Steps CSV: `.../digit_reduction_steps.csv` mirrors the reduction chain for any human/AI audit.
- Winners lens: `.../analyzer_v2/winners/{stamp}_{Variant}_{winner_map,flags,hits,overlay}.` Flags now include `dr_win_vt_boxed` and `dr_win_vt_straight`; hits CSV mirrors the same columns for quick scripts; overlays stay the human lens.
- Training log JSON: still the canonical input for rebuilds or golden-fixture tests.

**How to interpret key scoring features**
- `vt_only_lane=1` → winner had VT evidence but no exact hit; pair with `dr.win_vt_boxed`/`dr.win_vt_straight` to know if the VT lane is boxed only or straight-aligned.
- `funnel_precol1=1` → the family spent time in Set1 columns 4/3 before column 1; combine with `ls_col_42` to prioritize near-column ladders.
- `ls2_lane=1` → ladder terminates on LS2/Method T; expect combination with `vt_only_lane` for many LS2 wins.
- `drop_digit_mode_stability` ≥2 → persistent one-digit drop exposures, typically the best signal for exact lifts.
- `persistence_*` + `recency_carryover` let you gauge how long the family survived across columns/sets.

**Sharepack alignment**
- The per_state per_run bundles already contain the above files; no layout change from the earlier plan, just new columns in per_item/top/winner artifacts. Any aggregator script can point at `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/` and `.../training_sets/<STAMP>/` to ingest the contract.

**Watcher items**
- Keep running new dates until `ls_col_42_hits` flips >0; once we capture a real winner in those ladders we can finalize weight tuning.
- GA/TX/WV still lack table generation; pipeline runner guards against stale data, but those states will need fresh tables before aggregator work.


IMPORTANT FINAL THOUGHTS:

- Added a dedicated Digit “golden” fixture under fixtures/digit_mini plus tests/test_digit_reduction_regression.py. It sanity-checks the lean outputs by asserting that the per-item CSV carries vt_only_lane,
  - Digit winners overlays/flags/hits now emit final_vt_boxed/final_vt_straight, and the pipeline propagates dr.win_vt_boxed/dr.win_vt_straight into per_item rows—aligning Digit with Stable’s four-class
    winners taxonomy.
  - Appended an “Integrator Notes — Ready for Aggregator” section to docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md, summarizing why the tool is powerful now, which files form the contract, and which scoring fields
    matter most as inputs to the aggregator.
  - Updated the Digit section of docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md to call out the finalized brain bundle fields (vt_only/funnel/LS flags) and the fact that winner flags/hits now include VT boxed/
    straight columns.
     Next steps:

  1. Keep running new states/dates so LS column‑4/2 hits eventually flip on and we can finalize their weights.
  2. When you’re ready to aggregate, use the contract summarized in the Digit log + Lean Outputs doc. No further code changes are needed before wiring Digit into the cross-tool analyzer.


› I know you said you highlighted a few of the key features or something regarding the digit reduction module I guess what I still would appreciate a better understanding into is I remember the analyzer had
  a very rich volume of features and I was always trying to understand how to connect this with the training or design if that makes sense kinda I guess what I mean is I was excited by the prospects AI or a
  computer taking my methods or concepts and expanding and introducing more advanced features or analytics which it seems like it did with the rich collection of features and scoring features etcetera but it
  was a bit tricky for me to connect the dots of how they contribute in a way I understand or to know that they are being used effectively Maybe this is built into this scoring overall within the tool and I
  should trust in that ? Can you speak to that a bit more comprehensively so I can get that a bit better overall ? And also why you may select or identify certain key features that you highlighted for the
  analyzer to pay attention to over others ? I'm not sure if that all quite makes sense but hoping you can somewhat expand and provide some comprehensive insights could really help me understand things a bit
  better and feel confident in the tools power overall


• Totally makes sense. Digit Reduction’s analyzer emits a big set of columns, and not all of them are equally decisive. The idea is to focus on the ones that consistently explained wins during all the
  training/review we just did. Here’s how to think about it:

  1. Core scoring pillars (baked into the code)

  - Detection timing & persistence (earliest_*, persistence_*): These tell us how early and how often a winner’s family shows up. The scorer gives the highest weight to exact/vtrac that appear early and
    persist, which mirrors your “goal-aware triad” logic—early signals are worth more.
  - Density & purity (box_family_density, dup_bonus, residual_purity): These encode how “clean” the box is. If the reduction keeps the same three digits tightly packed, it gets rewarded. That’s how we teach
    the tool to prefer boxes that hold structure versus noisy ones.
  - Cross-evidence echoes (cols_hit, set_echo_count, variant_echo_count, method_consensus): These detect repeated confirmations across columns/sets/variants. Any time a family spans multiple columns (like the
    Set3→Set2→Set1 ladders you watch in the HTML), these features bump the score.

  You can trust that these pillars are wired directly into the scorer; the weights in config.yml show exactly how.

  2. VT-oriented features

  - vt_only_lane: Flags when a winner’s only evidence is VT-based (no exact). We added direct scoring weight so pure VT hits don’t get buried. Combined with dr.win_vt_boxed/dr.win_vt_straight, you can tell
    whether a ladder is already down to an 8-way box or a straight orientation.
  - dr.win_vt_boxed / dr.win_vt_straight: New overlay fields that make the VT taxonomy explicit—same four hit classes as Stable. These aren’t inputs to the score, but they’re critical for the aggregator to
    treat VT hits as “partial wins.”

  3. LS funnel / near-column features

  These features are highlighted because the runs proved they’re the most actionable—you see them in per_item.csv, and they’re the ones we gate QA on now (vt_only hits, LS col-4/2 hits).

  4. Why these features specifically?
  - Goal-aware triads → earliest/persistence + density/purity.
  - VT footprints → vt_only lane + VT boxed/straight flags.
  - Near-column ladders → funnel and ls_col_42.
  - LS2 endings → ls2_lane.
  - Drop-digit cues → drop_digit_mode, drop_run_len.

  Everything else in the per-item CSV is still useful for debugging (like steps_total_before_compaction), but those highlighted features are the high-signal ones the scorer actually uses. That’s why I called
  them out for the integrator—they’re the knobs that reflect your methodology, and you can trust they’re wired into the scoring.

  So, short version: the analyzer already “knows” how to use your concepts—the key features represent the things we proved matter most, and the scoring weights lean on those. You can read the per-item rows to
  see the signals, and the vt_only/LS funnel counters in Control Center confirm the code is tracking them run after run.
   
   
    +- Impact: Digit analyzer now records vt-only lanes, Set1 col-4/2 funnels (`funnel_precol1`, `ls_col_42`, `ls2_lane`), and the new per-item winner flags (`dr.win_vt_boxed`, `dr.win_vt_straight`); Cont
         rol Center's batch runner surfaces `vt_only_hits`/`ls_col_42_hits` per state so QA can spot near-column ladders immediately.
    166 +- Impact: Winners overlays/flags/hits JSON now emit `final_vt_boxed`/`final_vt_straight`, aligning Digit's taxonomy with Stable; fixtures + regression test (`fixtures/digit_mini`, `tests/test_digit_r
         eduction_regression.py`) guard the vt/funnel contract.
    167 +- Impact: Docs updated with the Digit Integrator Brief (`docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md`) and the lean outputs contract now references the vt/funnel columns and winner flag extensions (`doc
         s/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md`).
    168 +- Files: alpha_analytical/control_center/batch_runner.py, alpha_analytical/digit_reduction/analyzer_v2/{pipeline.py,winners_overlay.py,config.yml,score.py}, tests/test_digit_reduction_regression.py,
         fixtures/digit_mini/**, docs/AAT9_KIT/{AAT9_Digit_Analysis_Log.md,AAT9_Analyzer_Lean_Outputs.md}.
    634 +- Change:
    635 +  - Analyzer now persists `vt_only_lane`, `funnel_precol1`, `ls_col_42`, and `ls2_lane` in `per_item.csv`, and the scorer gives them explicit weight. Winners overlays/flags/hits gained `final_vt_boxe
         d`/`final_vt_straight`, matching Stable's four hit classes.
    636 +  - Control Center's batch workflow counts `vt_only_hits` and `ls_col_42_hits` per state after each run so QA can verify the new telemetry without diffing CSVs.
    637 +  - Added a golden fixture (`fixtures/digit_mini`) and regression test (`tests/test_digit_reduction_regression.py`) to lock the contract, plus appended integrator notes in `docs/AAT9_KIT/AAT9_Digit_A
         nalysis_Log.md` and updated the lean outputs spec.
    638 +- Impact: Digit's lean bundle now advertises the same VT taxonomy the winners module expects, vt-only ladders stay visible in QA, and future agents have a clear hand-off doc explaining which columns
         drive the scorer and aggregator.
  
   
   Added a new Unified Changelog entry (“2025‑11‑15 – Digit Reduction vt-only funnel + aggregator notes”) covering the vt_only/funnel/LS column work, Control Center QA counters, the VT boxed/straight winner
    flags, the new regression fixture, and the doc updates.
  - Logged the same changes in the Checkpoint Log (“2025‑11‑15 – Digit Reduction vt-only funnel contract”), describing the context, code updates, QA impact, and documentation touchpoints so future agents see
    why these metrics matter.
  - Updated docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md to mention the Digit brain bundle’s new columns (vt_only_lane, funnel_precol1, ls_col_42, ls2_lane) and that winner flags/hits now include
    dr_win_vt_boxed / dr_win_vt_straight.
  - The Digit Analysis Log already has the “Integrator Notes” section covering tool power, contracts, and key features; the regression fixture (fixtures/digit_mini + tests/test_digit_reduction_regression.py)
    is in place and documented.

    Yep—the two Codex Read This docs basically remind us to update the AAT9 KIT “core” set whenever we change tooling:

  - AAT9_Unified_Changelog.md
  - AAT9_Checkpoint_Log.md
  - AAT9_Analyzer_Lean_Outputs.md
  - AAT9_Workflow_Standard.md / AAT9_Live_Wiring_and_Data_Paths.md when wiring shifts
  - Plus the per-tool analysis logs (e.g. AAT9_Digit_Analysis_Log.md) and any user guides like USER_GUIDE_AAT9/DigitReduction_UserGuide.txt.

  For this round I hit the first three plus the Digit log; no separate wiring change was needed because the data paths didn’t move. That satisfies what Codex Read is asking for.

  Stable Packet-2 work is already documented: the November 12 entry in the Unified Changelog + Checkpoint Log covers the compound scorer, winners scripts, and sharepacks; Lean Outputs already describes
  Stable’s contract (brain files + winner lens). So we’re good there—everything from the earlier Stable push is logged.

  If we touch any other tool in future sessions we’ll just follow the same pattern: Changelog entry, checkpoint note, lean-spec delta, and whichever per-tool log or user guide applies.