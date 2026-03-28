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
