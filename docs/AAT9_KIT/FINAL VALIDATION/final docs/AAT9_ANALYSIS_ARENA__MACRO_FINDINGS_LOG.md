# AAT9 Analysis Arena Macro Findings Log

Purpose:

- keep the strongest cross-window Analysis Arena findings in one append-only place
- separate provisional findings from repeated findings
- preserve the best reverse-engineer-wins lessons for later scoring, Brain 2, translator, and budgeting work

Status tags:

- `PROVISIONAL`: seen in one window; do not promote yet
- `REPEATED`: seen in multiple windows
- `DEFERRED`: important, but not ready for promotion
- `CONTRADICTED`: a prior idea weakened or failed in a later window

How to use this log:

- append only after a full window is complete
- reference the exact window and primary artifact(s)
- keep each finding short, specific, and evidence-led
- do not promote new scoring logic from this file alone

---

## Entry Template

### Finding ID
- status:
- window(s):
- category:
- summary:
- evidence:
- implication:
- next test:

---

## Findings

### F-001
- status: `PROVISIONAL`
- window(s): `2026-01-05_to_2026-01-09`
- category: `Arena vs control-arm opportunity gap`
- summary: The rebuilt arena preserved materially more winner truth than the legacy downstream arm fully expressed.
- evidence:
  - winner reached board/audit surface on `138/138` events
  - Candidate Universe exact / box containment improved versus legacy same-window baseline
  - same shared legacy downstream strategies usually improved when replayed on arena-era sharepacks, especially at `B24/B36`
- implication: The main bottleneck is still downstream realization, not total signal absence.
- next test: Check whether the same gap repeats on the next comparison window and whether the lift again concentrates at `B24/B36`.

### F-002
- status: `PROVISIONAL`
- window(s): `2026-01-05_to_2026-01-09`
- category: `Hit morphology`
- summary: Doubles and mirror-double structure remained one of the strongest concrete hit contexts.
- evidence:
  - `57/94` credited hits were double-shaped
  - `55/57` of those graded `MEDIUM` or `STRONG` on double context
- implication: Double pressure is still a first-class context family and should remain explicit in hit analysis, scoreboard review, and future translator-learning work.
- next test: Check whether strong double-context concentration repeats on the next fully aligned window.

### F-003
- status: `PROVISIONAL`
- window(s): `2026-01-05_to_2026-01-09`
- category: `Brain 2 ranking`
- summary: Brain 2 state targeting still does not show enough edge yet, even though the upstream arena truth improved.
- evidence:
  - top3 / top5 / top1 state-containment rates were near random baseline
  - median board rank for all credited hits was `7.0`
  - median board rank for higher-conviction hits was `8.5`
- implication: Ranking/scoring refinement should focus on better state discrimination, not just richer context capture.
- next test: Compare hit-rank distribution and top-state containment on the next comparison window before changing Brain 2 scoring.

### F-004
- status: `PROVISIONAL`
- window(s): `2026-01-05_to_2026-01-09`
- category: `Winner frontier behavior`
- summary: Winner HTML frontier behavior was dominated by hidden-compressed, VTRAC, and feeder-to-frontier signatures, while literal frontier cases were rare.
- evidence:
  - signature mix: `HIDDEN_COMPRESSED_FRONTIER` x48, `VTRAC_FRONTIER` x44, `FEEDER_TO_FRONTIER` x37, `FAMILY_FRONTIER` x8, `LITERAL_FRONTIER` x1
  - average `vertical_stability_score` was high at `0.925`
  - promotion queue pointed to hidden compressed, feeder progression, and double-anchored compression
- implication: Future scoring and translator work should not assume literal late-frontier survival is the main winner form.
- next test: Re-run the frontier harness on the next window and see whether literal frontier remains rare.

### F-005
- status: `PROVISIONAL`
- window(s): `2026-01-05_to_2026-01-09`
- category: `Arena explicitness`
- summary: Explicit arena calls were sparse but sharp.
- evidence:
  - `arena_box_signal` fired on a small subset of events but was strongly enriched among converted hits
  - `arena_exact_signal` was very sparse and converted cleanly when present
- implication: A sparse high-precision arena layer may already exist, but it is not yet broad enough to define the whole realization layer.
- next test: Track precision and recall of explicit arena signals on the next window before broadening them.

---

## Open Questions

- Does the arena-vs-control-arm gap repeat on another comparison window with different draw character?
- Are doubles/mirror doubles still dominant when the window is not centered on the early-January span?
- Does the frontier harness keep showing hidden-compressed and feeder-driven survival as the dominant winner form?
- Can Brain 2 ranking improve through evidence-led changes without making the board more generic or static?

---

## Window Append: `2026-01-15_to_2026-01-18`

### F-006
- status: `REPEATED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Arena vs control-arm opportunity gap`
- summary: The arena-vs-downstream realization gap repeated on the second comparison window, and same-window Candidate Universe containment again improved versus the legacy baseline.
- evidence:
  - second-window Candidate Universe exact / box improved from legacy `18.5% / 27.2%` to arena `23.9% / 30.3%`
  - second-window Play Card any-box realization was still only `10.1%`
  - both windows kept `winner_on_board` at `100%`, while downstream realization remained much lower
- implication: The main bottleneck is still downstream expression and narrowing, not lack of upstream arena truth.
- next test: Track whether this same gap persists on a third comparison window before designing translator or budgeting replacements.

### F-007
- status: `REPEATED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Hit morphology`
- summary: Doubles and mirror doubles remained one of the strongest repeated hit contexts across both aligned windows.
- evidence:
  - first window: `57/94` credited hits were double-shaped, with `55/57` graded `MEDIUM` or `STRONG`
  - second window: `51/79` credited hits were double-shaped, with `48/51` graded `MEDIUM` or `STRONG`
  - mirror-double inventory remained materially present in both windows
- implication: Double pressure should stay explicit in hit analysis, scoreboard review, and future translator/scoring research.
- next test: Break double pressure into sub-types to see whether literal doubles, mirror doubles, or paired-family doubles carry the most useful lift.

### F-008
- status: `REPEATED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Brain 2 ranking`
- summary: Brain 2 ranking is still not separating the best hit-bearing states sharply enough, even after the arena rebuild and wrapper alignment.
- evidence:
  - top-primary target among winner events stayed near flat at `10/138` (`7.2%`) and `8/109` (`7.3%`)
  - median board rank for all credited hits stayed at `7.0` in both windows
  - second-window higher-conviction hit rank improved from `8.5` to `6.0`, but still did not produce strong top-state concentration
- implication: Ranking/scoring refinement should continue to focus on better state discrimination instead of adding more context layers without sharper prioritization.
- next test: Compare score components on hit-bearing mid-board states against missed top-ranked states before changing Brain 2 weights.

### F-009
- status: `REPEATED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Winner frontier behavior`
- summary: Winner HTML frontier behavior again favored hidden-compressed, feeder-to-frontier, and VTRAC corridor signatures rather than literal late-frontier survival.
- evidence:
  - first window frontier mix: `HIDDEN_COMPRESSED_FRONTIER` x48, `VTRAC_FRONTIER` x44, `FEEDER_TO_FRONTIER` x37, `LITERAL_FRONTIER` x1
  - second window frontier mix: `HIDDEN_COMPRESSED_FRONTIER` x50, `VTRAC_FRONTIER` x28, `FEEDER_TO_FRONTIER` x26, `LITERAL_FRONTIER` x0
  - both windows produced the same promotion queue themes:
    - hidden compressed winner-family frontier
    - feeder-to-frontier progression
    - double-anchored frontier compression
- implication: Literal frontier survival should not be treated as the default winner expectation; hidden family/VTRAC/compressed corridor behavior looks more central.
- next test: Compare these winner-frontier signatures against non-winning HTML cases before promoting any of them into live predictive scoring.

### F-010
- status: `REPEATED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Arena explicitness`
- summary: Explicit arena calls are still sparse, but they continue to look meaningfully sharper than ambient support layers when they do fire.
- evidence:
  - `arena_box_signal` remained small in both windows (`10/138` then `12/109`)
  - `arena_exact_signal` remained extremely sparse (`3` events in each window)
  - second-window high-conviction lift for both arena-explicit signals stayed high at about `2.95x`
- implication: A sparse high-precision arena layer likely already exists, but it is still too narrow to serve as the whole realization layer.
- next test: Track explicit-signal precision and recall across another window before broadening or reweighting those signals.

### F-011
- status: `PROVISIONAL`
- window(s): `2026-01-15_to_2026-01-18`
- category: `Hit cost profile`
- summary: The second window showed a somewhat healthier cost profile for higher-conviction hits, even though overall downstream realization remains weak.
- evidence:
  - second-window high-conviction box-any budget floor split was `B12:9`, `B24:10`, `B36:18`
  - second-window higher-conviction median rank improved to `6.0` from the first window’s `8.5`
  - control-arm-only catches fell from `18` to `14` while `CANONICAL_BOX` hits rose from `18` to `21`
- implication: The system may be starting to express a slightly cleaner higher-conviction layer, but the sample is too small to treat that as durable yet.
- next test: See whether a third window keeps pushing high-conviction hits toward cheaper budgets and better-ranked states.

### F-012
- status: `DEFERRED`
- window(s): `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`
- category: `Instrumentation / surfacing`
- summary: Some of the strongest Aux / Control Center indicators were preserved in machine-readable artifacts but still underexposed in the human state-review shell and under-aggregated at window close.
- evidence:
  - raw Aux summary and arena objects already preserved per-variant pair badges, boxed-combo badges, cross-variant overlap alerts, badge-pressure indices, and due-VTRAC overlays / heatboards
  - daily Brain 2 review already carried Blackapple / profit-alert / compound / due-double / repeat-watch context, but the window-close rollup was still mostly coarse
- implication: Before the next comparison windows, improve visibility and structured aggregation rather than assuming the underlying signal is missing.
- next test: Confirm that per-state Master Validation now shows explicit Aux inventories and that the deep window report rolls up the new daily tracker ledger across the next comparison windows.

---

## Window Append: `2025-12-30_to_2026-01-04`

### F-013
- status: `CONFIRMED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-15_to_2026-01-22`
- category: `Instrumentation / surfacing`
- summary: The explicit Aux-inventory and daily tracker-ledger upgrade is now confirmed in live comparison windows, not just in code.
- evidence:
  - per-state validation reports now expose `### G1a. Explicit Aux badge inventory` plus cross-variant pair overlaps and due-VTRAC overlay lists
  - [2025-12-30__Connecticut4.md](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/VALIDATION/2025-12-30__Connecticut4.md) and [2026-01-15__Connecticut4.md](/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL%20VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/VALIDATION/2026-01-15__Connecticut4.md) both show cross-variant overlaps and Combined / Midday / Evening due-VTRAC overlays
  - deep window analysis now reports full ledger coverage at `6/6` daily ledgers for the December window and `8/8` for the long January window
  - deep window analysis now rolls up Blackapple ALERT states and other tracker families instead of only coarse counts
- implication: Strong Aux / Control Center indicators are now visible enough to be audited, mined, and fed into later translator or Brain 2 research instead of being trapped in raw sidecar files.
- next test: Keep requiring full tracker-ledger coverage on each future window and make sure any new translator-learning ledger consumes these structured rollups instead of markdown prose.

### F-014
- status: `REPEATED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`, `2026-01-15_to_2026-01-22`
- category: `Pure arena finalist layer`
- summary: A real arena-native finalist layer is now repeating across windows even before a rebuilt combo/budget arm exists.
- evidence:
  - candidate-like event coverage stayed in a narrow band across the completed aligned windows: `39.3%`, `37.7%`, `45.9%`, `40.7%`
  - VT-like finalist coverage stayed material across the same windows: `37.4%`, `22.5%`, `42.2%`, `38.5%`
  - finalist-supported credited hits stayed high in every completed aligned window: `81/103` (`78.6%`), `76/94` (`80.9%`), `65/79` (`82.3%`), `118/142` (`83.1%`)
  - strict box hits with finalist support stayed very high: `10/10`, `10/12`, `11/11`, `11/12`
  - straight hits with finalist support also stayed very high: `19/20`, `16/18`, `16/16`, `27/30`
- implication: Analysis Arena is already producing real finalist/candidate-like information; the project does not need to wait for the combo/budget rebuild to start measuring meaningful upstream value.
- next test: Formalize the translator-learning ledger around `arena_final_candidate_signature`, `arena_box_signal`, `sandbox_box_seed`, and frontier corroboration so this finalist layer can be converted more deliberately.

### F-015
- status: `MIXED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`, `2026-01-15_to_2026-01-22`
- category: `Arena vs legacy comparison uplift`
- summary: Same-window legacy uplift is real on some windows, but it is not yet uniform across all window character.
- evidence:
  - December window was essentially flat on Candidate Universe containment: legacy exact/box `15.95% / 22.70%` vs arena `15.3% / 22.7%`
  - `2026-01-05_to_2026-01-09` improved to `20.3% / 24.6%` from legacy `18.1% / 22.5%`
  - short January bridge window improved to `23.9% / 30.3%` from legacy `18.5% / 27.2%`
  - long January window kept a modest exact improvement but slight box regression: legacy `13.9% / 24.2%` vs arena `15.4% / 23.1%`
  - Play Card any-box realization still stayed weak across all completed aligned windows: `6.1%`, `8.7%`, `10.1%`, `5.4%`
- implication: The arena is already strong enough to outperform the old arm in some windows, but cross-window replay is still unstable enough that downstream translation and ranking work remain necessary before expecting uniform uplift.
- next test: Build the cross-window comparison rollup so replay uplift can be broken down by draw character, hit morphology, and frontier signature instead of treated as one aggregate number.

---

## Window Append: `2026-01-15_to_2026-01-22`

### F-016
- status: `REPEATED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-22`
- category: `Translator opportunity-gap teaching set`
- summary: The longer January window materially expanded the explicit box-opportunity teaching set while keeping arena box evidence attached to every gap row.
- evidence:
  - December produced `5` `opportunity_gap_box` rows, the early-January window produced `5`, and the long January window produced `11`
  - in the long January window, explicit arena box support was present on `11/11` gap rows
  - long January also kept `arena_primary_box` on `8/11` gap rows and `sandbox_box_seed` on `7/11`
  - `3/11` of the long-January gap rows were still ranked inside the board top-5
- implication: The translator-learning problem is no longer abstract; there is now a substantive set of “arena knew box territory but the old arm missed” rows that can be preserved and studied directly.
- next test: Start the translator-learning ledger from the canonical windows first, using these gap rows as the initial teaching cohort before any live translator changes are attempted.

### F-017
- status: `REPEATED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`, `2026-01-15_to_2026-01-22`
- category: `Brain 2 ranking`
- summary: Brain 2 ranking still is not concentrating the best hit-bearing states near the top of the board, and the larger January window confirmed that this is not just an early-January quirk.
- evidence:
  - top-primary-target hit rates stayed effectively flat across the completed aligned windows: `7.4%`, `7.2%`, `7.3%`, `7.2%`
  - median board rank for credited hits stayed mid-board or worse: `7.0`, `7.0`, `7.0`, `8.0`
  - high-conviction median rank improved on the short January bridge (`6.0`) but the long January canonical window still sat at `7.0`
  - the long January window still placed `66/142` credited hits in the `LOW_BOARD` tier versus only `25` in `TOP3`
- implication: Ranking discrimination remains the cleanest scoring problem to solve next; the board is preserving useful truth, but it is still not prioritizing it sharply enough.
- next test: Run the planned Brain 2 ranking diagnostic against the canonical comparison windows and compare false-positive top states against hit-bearing mid-board states before changing any weights.

### F-018
- status: `REPEATED`
- window(s): `2025-12-30_to_2026-01-04`, `2026-01-05_to_2026-01-09`, `2026-01-15_to_2026-01-18`, `2026-01-15_to_2026-01-22`
- category: `Winner frontier behavior`
- summary: The frontier harness now has repeated support across the broader comparison corpus: hidden-compressed, feeder, and VTRAC frontier behavior remain dominant while literal frontier remains effectively absent.
- evidence:
  - December signature mix: `HIDDEN_COMPRESSED_FRONTIER` x62, `FEEDER_TO_FRONTIER` x49, `VTRAC_FRONTIER` x44, `FAMILY_FRONTIER` x8
  - early January signature mix: `HIDDEN_COMPRESSED_FRONTIER` x48, `FEEDER_TO_FRONTIER` x37, `VTRAC_FRONTIER` x44, `LITERAL_FRONTIER` x1
  - short January bridge signature mix: `HIDDEN_COMPRESSED_FRONTIER` x50, `FEEDER_TO_FRONTIER` x26, `VTRAC_FRONTIER` x28, `FAMILY_FRONTIER` x4
  - long January signature mix: `HIDDEN_COMPRESSED_FRONTIER` x91, `FEEDER_TO_FRONTIER` x65, `VTRAC_FRONTIER` x54, `FAMILY_FRONTIER` x10
  - literal frontier remained absent or nearly absent across the aligned windows
- implication: Future translator and frontier research should be built around hidden-compressed family/VTRAC survival and feeder progression, not around a literal late-frontier expectation.
- next test: Run the negative-control frontier study before promoting any of these signatures into live scoring or translator logic.
