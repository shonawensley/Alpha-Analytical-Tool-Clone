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
python3 scripts/tools/create_analysis_arena_stage3_decision_workbench.py --force
python3 scripts/tools/create_analysis_arena_stage4_fixture_replay_harness.py --force
python3 scripts/tools/create_analysis_arena_stage4b_replay_readback.py --force
python3 scripts/tools/create_analysis_arena_stage4c_shadow_translator_prototype.py --force
python3 scripts/tools/create_analysis_arena_stage5_shadow_translator_fixture_evaluator.py --force
```

Cycle-wrapper equivalents for Stage 3, Stage 4, Stage 4B, Stage 4C, and Stage 5:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py stage3-decision-workbench --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force
python3 scripts/tools/run_analysis_arena_cycle.py stage4-fixture-replay --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force
python3 scripts/tools/run_analysis_arena_cycle.py stage4b-replay-readback --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force
python3 scripts/tools/run_analysis_arena_cycle.py stage4c-shadow-translator --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force
python3 scripts/tools/run_analysis_arena_cycle.py stage5-shadow-evaluator --runs2-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2" --force
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
- Stage 3 decision workbench Markdown/JSON.
- Stage 3 promotion registry CSV.
- Stage 3 replay queue CSV.
- Stage 3 negative-control map CSV.
- Stage 3 evidence-utilization matrix CSV.
- Stage 3 decay stratification CSV.
- Stage 3 fresh-window decision readiness Markdown.
- Focus-window Stage 3 casebook Markdown/CSV when priority cases exist.
- Stage 4 fixture replay scorecard Markdown/JSON.
- Stage 4 fixture replay ledger CSV.
- Stage 4 replay decision registry CSV.
- Stage 4 mechanism-family scorecard CSV.
- Stage 4 source A / source B / overlap comparison CSV.
- Stage 4 yield and concentration matrix CSV.
- Stage 4 shared-lineage audit CSV.
- Stage 4 negative-control replay summary CSV.
- Stage 4 cycle receipt Markdown.
- Stage 4B replay readback Markdown/JSON.
- Stage 4B primitive cluster registry CSV.
- Stage 4B survivor/support/restraint casebook Markdown/CSV.
- Stage 4B leave-one-window-out holdout matrix CSV.
- Stage 4B translator design queue CSV.
- Stage 4B cycle receipt Markdown.
- Stage 4C shadow translator prototype Markdown/JSON.
- Stage 4C prototype rule registry CSV.
- Stage 4C lane separation matrix CSV.
- Stage 4C support gate effects CSV.
- Stage 4C restraint application audit CSV.
- Stage 4C holdout prototype scorecard CSV.
- Stage 4C translator prototype casebook Markdown/CSV.
- Stage 4C cycle receipt Markdown.
- Stage 5 shadow translator fixture evaluator Markdown/JSON.
- Stage 5 value completeness audit CSV.
- Stage 5 value-level replay ledger CSV.
- Stage 5 prototype mode scorecard CSV.
- Stage 5 source A / source B / overlap ablation matrix CSV.
- Stage 5 window stratification CSV.
- Stage 5 state stratification CSV.
- Stage 5 support-gate ablation CSV.
- Stage 5 restraint-effect audit CSV.
- Stage 5 `PRO_44` compliance checklist CSV.
- Stage 5 value-level casebook Markdown/CSV.
- Stage 5 cycle receipt Markdown.

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
14. Run the Stage 3 decision workbench after cross-window rollup.
15. Review the Stage 3 promotion registry, replay queue, negative-control map, evidence-utilization matrix, decay stratification, and focus-window casebook before proposing any scoring redesign.
16. Run the Stage 4 fixture replay harness after Stage 3.
17. Review Stage 4 by mechanism family first, then source A / source B / overlap lift, shared-lineage risk, yield, concentration, and negative-control restraint summaries.
18. Run the Stage 4B replay readback after Stage 4.
19. Review primitive clusters, casebook exemplars, leave-one-window-out outcomes, and the translator design queue before building any prototype translator.
20. Run the Stage 4C shadow translator prototype after Stage 4B.
21. Review the prototype rule registry, lane separation matrix, support-gate effects, restraint audit, holdout prototype scorecard, and casebook before any translator/scoring rewrite.
22. Run the Stage 5 shadow translator fixture evaluator after Stage 4C.
23. Review value completeness first, then prototype mode scorecard, ablation matrix, support-gate ablation, restraint-effect audit, window/state stratification, `PRO_44` compliance, and value-level casebook.
24. Use Stage 2, Stage 2B, Stage 3, Stage 4, Stage 4B, Stage 4C, and Stage 5 decisions as experiment gates, not live scoring changes.

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
- Stage 3 `promote_candidate` means replay permission only; it does not mean live scoring permission.
- Stage 3 `supporting_gate` means a signal may help when paired with sharper evidence, not that it should stand alone.
- Stage 3 `watch_decay_only` keeps VTRAC/territory strength in carryforward/context lanes until bounded boxed or exact evidence proves conversion.
- Stage 3 `negative_control` and denominator-control rows are assets for restraint, gating, and future penalty design.
- Stage 3 evidence-utilization rows answer whether a source family was available and winner-aligned; they do not prove the future Brain should weight that family directly.
- Stage 4 `survived_as_boxed_translator_candidate` means a bounded replay fixture survived for future translator design; it is not live-play permission.
- Stage 4 `survived_with_lineage_guardrail` means the fixture is useful but source A and source B are not independent enough to receive duplicate-credit scoring.
- Stage 4 source A / source B / overlap comparisons are mandatory before claiming an overlap adds value.
- Stage 4 `future_primitive` labels are architecture-facing abstractions; legacy source names remain locators only.
- Stage 4 concentration flags block fragile rules that are mostly carried by one state or a tiny set of state-days.
- Stage 4 negative-control summaries are future penalty/veto library candidates, not promotion candidates.
- Stage 4B primitive clusters collapse duplicate aliases and old-system locator variants; clusters are design units, not live rules.
- Stage 4B leave-one-window-out confirmation is a research filter. It improves confidence but still does not grant live scoring permission.
- Stage 4B translator design queue separates prototype candidates, duplicate-credit prototypes, support gates, decay/watch clusters, concentration retests, and low-denominator watchlists.
- Stage 4C prototype lanes are shadow design lanes only. They do not create deployable candidate lists or scoring weights.
- Stage 4C `clean_boxed_candidate` and `lineage_guarded_boxed_candidate` lanes are aggregate candidate-expression research surfaces, not live rules.
- Stage 4C support gates, decay/watch rows, concentration rows, low-denominator watchlists, and negative-control surfaces remain separated and cannot become standalone spend permission.
- Stage 4C old-system source names remain locators; the architecture-facing vocabulary is the primitive/lane/guardrail label set.
- Stage 5 value-level replay is a fixture evaluator only. It tests completed state-days and does not create deployable candidate lists.
- Stage 5 `value_level_complete` rows can support value-level claims; `sample_truncated` and aggregate-only rows must be treated as lower-precision evidence.
- Stage 5 support-gate and restraint-effect outputs are ablations. They can suggest future translator design, but they do not change live scoring or budget behavior.
- Stage 5 `PRO_44` compliance rows are acceptance checks for research discipline, not scoring approval.

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
- Do not use Stage 3 outputs to bypass replay. The workbench exists to prioritize replay, not replace it.
- Do not use Stage 4 to change live scoring directly. It is the controlled test bench before any translator/scoring rewrite.
- Do not blend all Stage 3 replay candidates into one pool; read Stage 4 by mechanism family.
- Do not treat arena, translation sandbox, Brain1, or old control-arm surfaces as independent confirmations when Stage 4 marks shared lineage risk.
- Do not build a prototype translator from raw Stage 4 rows when Stage 4B has collapsed them into primitive clusters.
- Do not treat Stage 4B holdout confirmation as final proof. It is a stronger filter, not a deployment gate.
- Do not treat Stage 4C as a scoring rewrite. It is a read-only shadow translator design package.
- Do not blend Stage 4C lanes. Candidate-expression, lineage de-duplication, support context, decay watch, restraint/retest, and low-denominator watchlist rows must stay separate.
- Do not treat Stage 5 as a scoring rewrite. It is the fixture-backed evaluator before any translator/scoring specification.
- Do not use Stage 5 value-level casebook rows as hand-picked rules; use the scorecards and denominators first.
- Do not claim value-level precision from Stage 5 rows marked `sample_truncated` or aggregate-only.
