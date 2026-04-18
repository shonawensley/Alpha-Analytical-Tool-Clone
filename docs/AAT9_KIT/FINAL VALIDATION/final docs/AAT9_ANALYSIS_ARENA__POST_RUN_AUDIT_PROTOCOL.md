# Analysis Arena Post-Run Audit Protocol

Purpose: make post-window learning repeatable, so high-value findings are not left only in narrative chat or one-off reports.

## 1. Required Inputs

- Completed Analysis Arena window root under `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`.
- Performance gap ledger.
- Hit roster.
- Translator learning ledger.
- C1/C2 frontier cases with non-zero case count.
- Decay carryover rows with tail coverage noted.
- Per-day board scoreboard JSON.
- Per-day translation sandbox seed manifest and seed JSONs.
- Stage 1 audit outputs before Stage 2 is run.
- Stage 2 outputs before Stage 2B is run.

## 2. Run Commands

```bash
python3 scripts/tools/create_window_evidence_utilization_audit.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_audit_interpretation_report.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_stage2_signal_exposure_audit.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_stage2b_signal_stack_analysis.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_stage2b_cross_window_stack_rollup.py --force
```

## 3. Required Outputs

- Evidence utilization ledger CSV.
- Evidence utilization audit Markdown/JSON.
- Winner signal attribution ledger CSV.
- Winner signal attribution scorecard Markdown.
- Case dossiers Markdown.
- Translator redesign lessons Markdown.
- Signal source dictionary Markdown.
- Audit interpretation pass Markdown/JSON.
- Audit interpretation priority cases CSV.
- Audit interpretation signal decisions CSV.
- Audit baseline SSOT Markdown/JSON.
- Stage 2 signal exposure ledger CSV.
- Stage 2 false-positive scorecard Markdown/JSON.
- Stage 2 signal promotion decision matrix CSV.
- Stage 2 lane sharpness report Markdown.
- Stage 2 translator fixture candidates CSV.
- Stage 2 audit interpretation Markdown/JSON.
- Stage 2 executive readout Markdown.
- Stage 2 source-family ranking CSV.
- Stage 2 denominator risk map CSV.
- Stage 2B signal pairing ledger CSV.
- Stage 2B signal stack scorecard Markdown/JSON.
- Stage 2B promotion candidates CSV.
- Stage 2B negative-control stacks CSV.
- Translator fixture deep review Markdown.
- Gap teacher stacks CSV.
- Wrong-lane restraint rules Markdown.
- Positive conversion regression set CSV.
- Decay carryforward teaching set CSV.
- Translator rule hypothesis queue Markdown/CSV.
- Stage 2 cross-window readiness Markdown.
- Stage 2B overnight work log Markdown.
- Stage 2B cross-window stack rollup Markdown/JSON.
- Stage 2B cross-window stack confirmation CSV.
- Stage 2B cross-window hypothesis confirmation CSV.
- Stage 2B cross-window source confirmation CSV.

## 4. Review Order

1. Confirm event count equals the window performance-gap denominator.
2. Confirm winner signal attribution has both pre-draw and post-result rows.
3. Review captured-but-underused and wrong-lane cases before judging final candidate quality.
4. Review box-gap and exact-gap dossiers as translator training examples.
5. Review source dictionary coverage before assuming an indicator was absent.
6. Run and review the audit interpretation pass before choosing future candidate/Brain scoring experiments.
7. Use interpretation priority cases as fixture candidates, not as immediate scoring weights.
8. Freeze the audit baseline SSOT before Stage 2 interpretation.
9. Review Stage 2 exposure denominators before promoting any signal.
10. Run Stage 2B stack analysis after Stage 2 denominators are frozen.
11. Review the executive readout, hypothesis queue, stack scorecard, and wrong-lane restraint rules before any translator experiment.
12. Backfill Stage 2 and Stage 2B onto older ready windows before treating any March-only stack as durable.
13. Run the cross-window stack rollup and separate candidates, support gates, VTRAC watch rows, negative controls, and low-denominator fixtures.
14. Use Stage 2 and Stage 2B decisions as experiment gates, not live scoring changes.

## 5. Interpretation Rules

- `CAPTURED_AND_USED` means evidence reached final conversion.
- `CAPTURED_BUT_UNDERUSED` means evidence existed but old final selection did not fully use it.
- `CAPTURED_BUT_WRONG_LANE` means territory/VTRAC support existed but boxed/straight conversion failed.
- `DECAY_VALIDATED` means same-day grading under-credits a signal that resolved inside the configured horizon.
- `BROAD_CONTEXT_ONLY` means a signal may be useful context but is not sharp enough alone.
- `NOT_CAPTURED` means no strong machine-readable evidence was found by current parser coverage.
- Audit interpretation counts are teaching-cohort labels. They do not replace raw performance totals.
- Stage 2 `false_positive_proxy` means an exposed value did not match a same-day winner in the completed window. It is a denominator, not final proof of uselessness.
- Stage 2B stack rows measure agreement between sources on the same state-day. They are translator hypotheses, not final master-score weights.
- Stage 2B pairing ledgers are exported as Git-safe drill-down rows; the full pair/state-day denominator count is retained in stack JSON metadata.
- Old candidate/play-card dominated stacks are useful controls and fixture material, but they are not proof that new Analysis Arena translation logic is already solved.
- Cross-window boxed translator candidates are replay candidates only. Low-denominator repeats must stay fixture/watch material even when their rate looks high.

## 6. Guardrails

- Do not redesign prediction/budget logic directly from winner-only attribution.
- Add false-positive exposure denominators before building a new master score.
- Keep bonus/fireball metrics separate from standard exact/box/VTRAC metrics.
- Keep Brain2 rank-static diagnostics active.
- Treat the interpretation pass as design guidance; scoring changes still require Stage-2 exposure/false-positive measurement.
- Treat Stage 2 promotion labels as candidate experiment gates until confirmed across more than one window.
- Treat Stage 2B hypothesis labels as replay targets until they pass bounded fixture tests and at least one cross-window confirmation.
- Do not promote broad VTRAC/context stacks without a bounded boxed or exact confirmation source.
- Do not rank by hit rate alone; require denominator size, event support, lane correctness, and cross-window behavior.
