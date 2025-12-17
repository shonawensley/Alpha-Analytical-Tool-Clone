# Master Validation – Final Template (Part A)

Purpose: read the 3-variant winners output (HTML + JSON) *before* any tool scoring. Use it as the environment lens to characterize the winning pattern and its family/VT context. Then answer the questions below to extract maximal analytical value.

Execution note (recommended):
- Do not write answers into this template file. Generate a per-run report and fill answers there:
  - `python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4`
  - Output: `tasks/FINAL VALIDATION/RUNS/YYYY-MM-DD__<STATE>.md`

How to read:
- Open the analyzer-style winners HTML for the state/date (Midday, Evening, Combined panes). If available, also skim the JSON twin for counts/index info.
- Observe how the winning pattern/family appears through the Set3→Set1 progression (R2/R4/R6/R8) and across variants. Note hot markers (*, **), colored overlays (winner, VT family/straight), and column positions (especially col1/col2).
- Think in terms of the 4 hit criteria (exact straight, exact boxed, VT-boxed, VT-straight) and “profitable environment” traits (cross-variant convergence, col1/2 density, clear lanes).
- Then answer Part A (questions 1–10), keeping it environment-only (no tool scores).

Part A — 3-variant winners HTML/JSON (environment lens)
1) Column‑1 ladders (Set1 R2/R4/R6/R8): How do Set1 col1 boxes relate to the winning pattern? Note cross‑variant family/VT presence and any star/hot markers.
2) Column‑1 persistence/hotness: How strongly do pattern clusters persist into col1/col2 (hot/super‑hot) and how does that tie to the winner?
3) Last survivors (3‑value + 3‑VTRAC): Identify the last remaining 3‑value and 3‑VT patterns across the R2/R4/R6/R8 progressions (Set3→Set1, Draw1→7). How do they relate to recent draw_data col1/2? Cross‑variant relationship?
4) Variant bias: Which variant carries the winner most strongly (Midday/Evening/Combined)? Are patterns converging across variants or leaning to one variant?
5) Permutation lane clarity: Is the straight lane clear/tight or diffuse? Are permutations clustered or scattered across columns/variants?
6) Environment verdict: Classify the environment as strong/support/weak based on convergence of variants, col1/2 density, and hot markers.
7) Hot Zones overlap: Do hotzone lanes (col3–5) overlap the winner’s family/VT lane (even when not starred in VTRAC)?
8) Cross‑set carryover: Does the same family repeat from Set3→Set2→Set1, reinforcing persistence?
9) Aux cues (optional quick note): Any obvious doubles/mirror/positional pressure visible in col1/2 worth logging as Aux evidence?
10) 4 hit criteria viability: Exact boxed / Exact straight / VT‑boxed / VT‑straight — is there a plausible path for each? Note permutation clues, straight lanes, or cross‑variant VT boxes. If none, state N/A.
11) Exact triple presence: Is the exact winning triple (boxed/straight) explicitly present in the string tables (which variant/set/column)? Does it cluster with the VT family? This helps gauge when we might cover in‑table permutations vs the full VT box.
12) Profitable environment summary: What concrete signals made this environment strong/weak (e.g., cross‑variant convergence, column‑1/2 density, clear straight lane, set carryover, VT box density)? Which of these look like repeatable “profitable environment” traits?
13) Dominance vs dilution: Does the winner’s family/VT cluster dominate the pattern occurrence/persistence stats (counts/tables) compared to others, or is it just one of many?
14) Noise check: Is the environment clean (one dominant family/lane) or noisy (many competing families/lanes/conflicting cues)? Any caution flags despite apparent heat?

---

# Part 2 — Per-Tool Analytical Output Review (Brain + Winners artifacts)

Purpose: for each string-table tool (Stable, Digit Reduction, VTRAC Analyzer, Hot Zones), distill the brain outputs + the tool’s winners artifacts into a concise analysis so another AI doesn’t need raw files. Mark validation-only items with “(V)” so they can be retired once stable. Keep winners outputs conceptually separate from brain outputs (brain = analyzer evidence; winners artifacts = post-results logging).

Prereqs / workflow references:
- If the sharepack + winners artifacts are not already generated for this date/state, follow: `docs/AAT9_KIT/AAT9_Final_Validation_Help.md` (entry) and `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md` (one-shot wrapper + guards).
- Sharepack convention: `sharepacks/<RESULTS_DATE>/<STATE>/...` (winners/results date D). Tables are built from the history workbook (typically D‑1), then evaluated against winners from D.
- Per-tool summarizers are intended to be the “paste block” that captures *all key evidence with source labels* (so we don’t paste raw CSVs). Generate/refresh `summary.md`, paste it under step 0), then answer Q1–Q10.

Before you start a tool, confirm you have reviewed *all* of its final outputs (brain vs winners, listed separately per tool). Add a quick “outputs reviewed” note at the top of each tool section.

- **Stable**  
  - Brain: patterns_scores.csv, patterns_families.csv, patterns_compound.csv, metrics.json, (optional) patterns_report.html, training_set bundle/manifest.  
  - Winners: winner_family_spotlight_raw.csv, winner_family_spotlight_families.csv.
- **Digit Reduction**  
  - Brain: digit_reduction_report.html + scores.csv, analyzer_v2 per_item.csv/top_candidates.csv/meta.json, stacked HTML, training logs/steps (JSON/CSV), overlays (maps/flags/hits) if present.  
  - Winners: winner_flags/hits/map (only if generated by diagnostics/batch).
- **VTRAC Analyzer**  
  - Brain: enhanced analyzer bundle (per_item/top/meta if emitted), compact_report.json/csv, summary.md/csv, validation report (if generated).  
  - Winners: winner_map.json/csv, winner_flags.csv (if produced), overlay HTML/ZIP if present.
- **Hot Zones**  
  - Brain: hot_zones_per_lane.csv, hot_zones_top_lanes.csv, hot_zones_meta.json.  
  - Winners: YYYYMMDD_hot_zones_winner_map.json/csv (and hits if emitted).

Use the template below per tool (copy/paste for each: Stable, DR, VTRAC, Hot Zones). Tip: paste the tool summarizer Markdown (if generated) under 0) before answering.

## 2.[Tool] — [State] [Date]
0) Outputs reviewed  
   - Brain: […]  
   - Winners: […]  
   - Missing?: …
   - Canonical note: tools often use canonical (sorted) forms. Map literal → canonical before filtering (e.g., 517 → 157). Summarizer helpers (paste their Markdown here, then answer Q1–Q10):
     - Stable: `python3 scripts/tools/stable_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/stable/<STATE> --md-out summary.md`
     - Digit Reduction: `python3 scripts/tools/dr_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/digit_reduction/<STATE> --md-out summary.md`
     - V-TRAC: `python3 scripts/tools/vtrac_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/vtrac/<STATE> --md-out summary.md`
     - Hot Zones: `python3 scripts/tools/hot_zones_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/hot_zones/<STATE> --md-out summary.md`
   - Reminder: consult both the lean outputs doc and the tool-specific analysis log for this tool (self-contained optimizations, final outputs, insights). This helps decide what to extract/label and confirms you’re covering all final outputs.
1) Winners evidence vs brain outputs  
   - Where does the winning triple/family appear in the brain outputs (scores/compound/families/metrics/spotlight or tool-equivalent)? Cite rank/score and key why-tags. If absent, note “not present.”
2) 4 hit criteria mapping  
   - Exact boxed / Exact straight / VT-boxed / VT-straight: plausible path? Where and what evidence? If none, N/A.
3) Winners output alignment  
   - Do the tool’s winners artifacts (maps/flags/spotlights) match the brain evidence? Any discrepancies?
4) Dominance / noise  
   - Does the winner’s family dominate counts/persistence, or is it one of many? Clean vs noisy environment inside this tool.
5) Top candidate clusters  
   - Brief list of top candidates the tool rated highest (canonical, rank, key why-tags). Note any alignment with the winner or the 4 criteria, and which look like “keep”/profitable signals worth favoring.
6) Miss analysis  
   - If the winner is low/absent, likely cause (e.g., weak col1 chain, VT-straight underweighted, consensus ignored). Keep concise.
7) Validation checks (V)  
   - (V) Data read/schema OK? (tables present, no errors)  
   - (V) Features/columns missing or scoring zero unexpectedly?  
   - (V) Winners/spotlight/metrics files written? If not, note the issue.
8) Optimization notes  
   - Specific fixes/tunings suggested by this run (e.g., boost VT-straight mid-cols, reward col2→col1 funnels, include literal winner in spotlight).
9) Cross-tool synergy seed  
   - Given this tool’s outputs and Part 1 environment, which clusters/signals should carry forward to combine with other tools? Do they reinforce/align with likely candidates or the 4 criteria? Any immediate aggregator rule ideas (e.g., “if Stable + DR both surface VT21 in col1/2, boost”)?
10) Analyst’s extra insights (optional but encouraged)  
    - Any analytically powerful observations that don’t fit above (e.g., profitable-environment traits, notable permutations/lanes, architectural wiring notes for separating brain vs winners modules).

After all tools are reviewed, add a short 2B wrap-up (optional):
- Cross-tool synthesis (all tools): list the top shared clusters/signals across tools for this date/state, note conflicts, and jot any aggregator/aux hooks to test.

---

# Part 3 — Aux Features (Environment + Compound Evidence)

Purpose: inventory the Aux signals for the same date/state (Combined/Midday/Evening) and log which signals align with (a) the actual winner and (b) the top candidate clusters from Part 2. This is **evidence-first**: we log signals + convergence now, and only later convert them into weights/rules (Strings lead, Aux compounds).

Key rule: Aux draws must be aligned to the **history workbook** used to build the string tables (typically D‑1 for results date D). If the workbook changes, Aux signals change. For master validation, we therefore snapshot the draw CSVs into the sharepack so Part 3 stays reproducible across sessions.

Evidence block (recommended):
- Generate/update the Aux summary inside the sharepack:
  - Recommended (history-aligned; prevents drift after workbook swaps):
    - `python3 scripts/tools/aux_sharepack_summary.py --date <DATE> --state <STATE> --excel data/history/Pick3StatsC4_<HISTORY_D-1>.xlsm`
  - Fallback (copies from current live `data/cleaned/draws`; use only if you don’t have the history workbook snapshot):
    - `python3 scripts/tools/aux_sharepack_summary.py --date <DATE> --state <STATE>`
- Paste the generated `summary.md` under 0) before answering Q1–Q10.

## 3.Aux — [State] [Date]
0) Outputs reviewed  
   - Draw CSV snapshot: `sharepacks/<DATE>/<STATE>/aux/draws/` (Combined/Midday/Evening)  
   - Aux evidence dump: `sharepacks/<DATE>/<STATE>/aux/<STATE>/summary.md` (all facts labeled by source)  
   - (Optional) UI cross-check: Aux page screenshots / captions (only if needed)
1) Aux input validation (V)  
   - Confirm the draw CSV paths used (original + snapshot), draw counts, and newest two draws per variant.  
   - Confirm those newest draws match the “world snapshot” implied by tables (e.g., Set1 Draw1/Draw2 columns in Combined table).
2) Positional pressure (core)  
   - For each variant: top due digits per position + any hard-due flags.  
   - Cross-variant consensus: digits that are top‑k in the same position across 2–3 variants (“XVAR consensus”).  
   - Does the winner (and/or top Part‑2 candidates) intersect these digits/positions?
3) Positional shortlist (prediction list)  
   - List the shortlist candidates + tags (top N).  
   - Any overlap with winner (literal/canonical) or Part‑2 top clusters? If no direct overlap, any “shared digits/positions” clues?
4) Repeat‑watch + index streak context  
   - Current repeat index / streak per variant + any notable “hard‑due” repeat conditions.  
   - Map the winner’s VTRAC index: is it due/repeating/avoided by this context?
5) VTRAC overlay / heatboard (index pressure)  
   - Which indices are most overdue/hot per variant? Any that compound across variants?  
   - Does the winner’s index sit in a high‑pressure zone? Do Part‑2 top clusters sit in those indices?
6) Doubles + pairs pressure  
   - Overdue doubles (canonical) and overdue pairs (repeat/non-repeat) per variant; call out multi-variant alerts.  
   - Does the winner (and/or Part‑2 top candidates) contain any of these overdue doubles/pairs?
7) Sums / root‑sum pressure  
   - Due sums / deficit flags per variant (and any cross‑variant compounds).  
   - Does the winner (or top candidates) align with due sum/root patterns?
8) Blackapple (if enabled)  
   - BA score + triggers per variant; list top BA candidates and tags.  
   - Does BA “agree” with the winner/candidate families or contradict them?
9) Aux convergence score (new, high‑value)  
   - Build a tiny table for (winner + top 5–10 candidates): number of Aux signals supporting it, and in how many variants (1/2/3).  
   - Highlight “high-confidence” candidates where Aux compounding is strongest across variants.
   - Suggested first‑pass “signal” types to count (keep it explicit with a legend):
     - `pos`: in positional shortlist
     - `idxTop`: candidate VTRAC index is in the variant’s top‑overdue overlay list
     - `sum`: candidate sum has a strong flag (red or blue)
     - `pair`: candidate contains a pending pair (red/blue/purple)
     - `BA`: candidate is a top Blackapple pick (if enabled)
10) How to apply Aux (design implications + expense lever)  
   - Should the strongest Aux signals here be used as state-level gating (“play day / pass day”), candidate-level boosts, or both?  
   - Given Part 1+2+3 evidence, what is the cheapest reasonable play mode (perm-only vs VT-box vs skip), and why?
