# AAT9 Analysis Arena Metric Legend

Purpose:

- stop layer-mixing when reading arena-era results
- define which metric families belong to which layer
- clarify what each family does and does not prove
- make headline metrics and diagnostic metrics explicit

Use this with:

- `AAT9_ANALYSIS_ARENA__HOW_TO_READ_FRESH_WINDOW_RESULTS.md`
- `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md`
- the current canonical comparison windows in `RUNS_2/`

## 1. Core Rule

Do not ask one metric family to answer everything.

Read the branch in layers:

1. Arena Truth
2. Brain 2 Prioritization
3. Control Arm Realization
4. Translator Opportunity
5. Policy / Budget implications only after the above

## 2. Baselines

Main teaching baseline:

- `WINDOW_2026-01-15_to_2026-01-22`

Secondary stability anchor:

- `WINDOW_2026-01-05_to_2026-01-09`

Use both when judging a fresh window so one long January block does not become the whole truth model.

## 3. Metric Families

| Metric Family | Layer | Judges | Headline? | Allowed Conclusion | Forbidden Conclusion | Baseline | Common Misuse |
|---|---|---|---|---|---|---|---|
| Winner canonical / family / VTRAC presence | Arena Truth | Whether Brain 1 preserved winner-side structure at all | Yes | The arena trapped meaningful winner-side structure | The final downstream system is already solved | Long January + secondary anchor | Treating preservation as final conversion |
| `arena_primary_vt`, `sandbox_vt_seed`, VT-like finalist coverage | Arena Truth | Whether the arena identified finalist/VTRAC territory | Yes | The arena is producing finalist-like evidence | The system already has finished combo expression | Long January + secondary anchor | Reading VT-like territory as final play geometry |
| `arena_box_signal`, `arena_exact_signal`, `arena_primary_box`, `sandbox_box_seed`, `sandbox_exact_seed` | Arena Truth | Whether the arena expressed explicit box/exact candidate-like pressure | Yes | The arena showed box/exact candidate-like structure | The old control arm executed it properly | Long January + secondary anchor | Blending explicit arena signals with Play Card outcomes |
| `arena_final_candidate_signature` and finalist-supported credited hits | Mixed: Arena Truth + realized-hit subset | Whether converted hits often had arena-native finalist support behind them | Yes, but as a support metric | Many converted hits were not control-arm-only accidents | The arena converts at that same rate into finished plays | Long January + secondary anchor | Reading support rate as final hit rate |
| Board rank, `top_primary_target`, `best_clean_host`, credited-hit rank distribution | Brain 2 Prioritization | How well Brain 2 ranked and concentrated the right states | Yes | Brain 2 prioritization is strong, flat, or weak | The arena did or did not trap truth overall | Long January + secondary anchor | Treating low top-primary rate as proof Brain 1 failed |
| Tier / band placement and concentration (`TOP3`, `TOP5`, `LOW_BOARD`) | Brain 2 Prioritization | Whether hits are concentrated in the right board bands | Yes | The board is or is not concentrating truth sharply enough | The control arm or translator is the main issue | Long January + secondary anchor | Mixing board concentration with old pack conversion |
| Candidate Universe recall / containment | Control Arm Realization | How the old downstream baseline preserved arena truth | Diagnostic headline for the old arm only | The old baseline retained or dropped arena-side structure | Candidate Universe defines arena quality | Long January + secondary anchor | Treating CU recall as pure arena truth |
| Play Card strict / boxed / any-box / any-exact | Control Arm Realization | How the old play-expression layer performed | Diagnostic headline for the old arm only | The old downstream arm converted weakly or strongly | The arena itself only knew that much | Long January + secondary anchor | Treating weak Play Card conversion as direct arena failure |
| `B12` / `B24` / `B36` | Control Arm Realization | How old budget geometry realized the old downstream playset | No, diagnostic only | The old budget stack expressed or missed what came downstream | Budget metrics define branch quality | Long January + secondary anchor | Using budget outcomes as the main branch score |
| `opportunity_gap_box`, box-gap rows, gap rows with arena box support, sandbox support | Translator Opportunity | Where the arena knew box territory and the old arm failed to express it | Yes | These rows are the core teaching set for future translators | These rows are failed arena rows | Long January primary, secondary anchor as check | Treating gap rows as simple misses instead of translator lessons |
| Translator-learning ledger cohorts (`BOX_GAP`, arena-explicit, VT-finalist) | Translator Opportunity | The size and character of the teaching cohort for later translators | Yes | The translator problem is concrete and measurable | A live translator already exists | Long January primary, secondary anchor as check | Treating the ledger as a live execution system |
| Decay / carryover scorecard (`same_day`, `horizon_resolved`, `incremental_decay_lift`, resolution profiles) | Companion: Arena Truth over time | Whether arena-side state-day snapshots resolve within a bounded future horizon | Yes, but only as a companion layer | Strong snapshots may resolve inside a short profitable horizon even when same-day misses stay cleanly separate | Same-day Arena truth and horizon-resolved decay are the same metric | Compare against the same window’s same-day package first, then use fresh windows | Blending delayed resolution into same-day headline rates |
| Frontier signature mix | Translator Opportunity / research | What structural winner-survival shapes repeat | Diagnostic only unless thresholded | Hidden/compressed or feeder/VTRAC structures are repeating research signals | Raw frontier presence should be promoted directly | Long January + frontier negative-control study | Promoting raw frontier presence into scoring |
| Frontier negative-control lifts | Translator Opportunity / research | Which frontier traits are discriminative versus ambient | Yes for frontier promotion decisions | Thresholded frontier traits are promotable research candidates | All frontier presence is predictive | Cross-window frontier control study | Ignoring the control study and promoting raw feeder/VTRAC presence |
| Tracker lift (`profit`, `Blackapple`, `due doubles`, `sandbox` support) | Mixed diagnostic | Which tracker families are sharp versus ambient | Diagnostic only | Some tracker families help ranking or translator work more than others | Every tracked signal deserves equal scoring weight | Tune-up diagnostics + fresh windows | Treating presence as the same thing as lift |
| Policy / budget implications | Policy / Budget | What future action, cap, or translator route might eventually make sense | No, not final yet | Future policy/budget work should be informed by upstream evidence | Current policy/budget is already the finished arena-native end state | Use only after all prior layers | Jumping to economics before reading truth, ranking, and opportunity |

## 4. Layer Notes

### Arena Truth

Use this layer to answer:

- did the arena preserve the winner-side environment?
- did it expose finalist or candidate-like structure?

Do not use this layer to claim:

- final budget success
- final play conversion quality

### Brain 2 Prioritization

Use this layer to answer:

- did the board rank the right states sharply enough?

Do not use this layer to claim:

- the control arm performed well
- the translator problem is solved

### Control Arm Realization

Use this layer to answer:

- what did the legacy downstream baseline do with arena-preserved truth?

Do not use this layer to claim:

- the arena only knew that much
- the branch’s final architecture should still look like the control arm

### Translator Opportunity

Use this layer to answer:

- where did the arena already know enough that a better translator should have acted differently?

Do not use this layer to claim:

- a live translator already exists
- the future translator rules are fully decided

### Decay / Carryover Companion

Use this layer to answer:

- did strong Arena-era state-day snapshots resolve later inside the configured horizon?
- how much of that was same-day carryforward versus true future-day decay?

Do not use this layer to claim:

- same-day Arena truth was stronger or weaker than it actually was
- delayed resolution should be blended into same-day headline metrics

## 5. Headline Rule

If a fresh-window discussion needs a short headline, keep it layered:

- Arena Truth verdict
- Brain 2 Prioritization verdict
- Control Arm verdict
- Translator Opportunity verdict

That is the correct summary shape for this branch.
