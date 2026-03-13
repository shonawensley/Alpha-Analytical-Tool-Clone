# DR Arena v1 - Broad Screen

Purpose: perform a wider, faster validation pass after the 11-case parity audit.

This is not a replacement for full harness fills.
It is a larger screening layer designed to answer:

- do the DR arena surfaces still hold up outside the 11 fully reviewed cases?
- which cases deserve the next manual deep-fill effort?
- which arena surfaces look stable, and which still look weak?

Source pool:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`

Method:
- selected `14` new cases across positives and controls,
- generated in-memory `DR Arena v1` payloads from frozen historical sharepacks,
- recorded whether the key surfaces remained active or sparse.

This raises the reviewed/screened evidence base from:
- `11` fully filled cases
to
- `25` total cases in scope.

---

## Screen table

| Case | Target class | Trace rows | Lane rows | Double rows | Sparse? | Cold locations | Read |
|---|---|---:|---:|---:|---:|---:|---|
| `2025-12-31 / Delaware4 / Evening / 337` | buried-trace | 10 | 10 | 10 | `False` | 7 | positive |
| `2026-01-07 / Delaware4 / Evening / 922` | buried-trace | 9 | 9 | 9 | `False` | 0 | positive |
| `2025-06-23 / Indiana4 / Midday / 110` | buried-trace | 8 | 8 | 7 | `False` | 0 | positive |
| `2026-01-02 / SouthCarolina4 / Midday / 308` | buried-trace | 10 | 10 | 10 | `False` | 8 | positive |
| `2025-06-23 / NewJersey4 / Midday / 106` | buried-trace | 10 | 10 | 8 | `False` | 29 | positive but cold-heavy |
| `2025-12-31 / Virginia4 / Midday / 686` | double-trace | 10 | 10 | 10 | `False` | 14 | positive |
| `2026-01-02 / PuertoRico4 / Midday / 144` | double-trace | 9 | 9 | 8 | `False` | 0 | positive |
| `2025-06-23 / NewYork4 / Evening / 767` | double-trace | 6 | 6 | 5 | `False` | 2 | positive but narrower |
| `2026-01-03 / Florida4 / Evening / 611` | double-trace | 8 | 8 | 4 | `False` | 14 | positive with weaker double surface |
| `2025-06-21 / Virginia4 / Midday / 473` | empty-control | 2 | 2 | 2 | `False` | 0 | control but still active |
| `2025-06-22 / OntarioCanada4 / Evening / 616` | empty-control | 5 | 5 | 5 | `False` | 4 | control but still active |
| `2025-12-31 / NewYork4 / Evening / 116` | empty-control | 10 | 10 | 10 | `False` | 7 | control but highly active |
| `2026-01-02 / Indiana4 / Evening / 359` | empty-control | 9 | 9 | 9 | `False` | 9 | control but highly active |
| `2026-01-05 / NewJersey4 / Evening / 694` | empty-control | 10 | 10 | 10 | `False` | 2 | control but highly active |

---

## Main findings

### 1. Positive classes are stable

The broader positives kept reinforcing the same arena surfaces:

- `dr_trace_strength`
- `dr_lane_only_confidence`
- `dr_double_pressure`

That means the 11-case design basis was not just a small-sample artifact.

### 2. `dr_empty_lens` is the weakest surface

This is the clearest result from the broad screen.

All five chosen controls still produced non-sparse DR arena sections.

That does **not** mean the arena is useless.
It means:

- the positive surfaces are easier to preserve than true negative-control behavior,
- and the next likely DR arena refinement should be:
  - **make `dr_empty_lens` much more discriminative.**

### 3. Cold-count alone is not enough

Some strong positives still carried high cold-location counts:

- `2025-06-23 / NewJersey4 / Midday / 106`
- `2025-12-31 / Virginia4 / Midday / 686`
- `2026-01-03 / Florida4 / Evening / 611`

So the fix cannot just be:
- “if cold count is high, call it empty.”

The next sparse-control logic needs to use:
- reveal quality
- current-band relevance
- row-repeat/final-survival
- stronger lane confidence
- maybe method concentration

### 4. The broader screen supports more data before redesign

The screen confirms that the right next design move is still:
- more validation and synthesis,
- not immediate DR analyzer surgery.

In particular, the broader screen supports:
- `DR Arena v1.1` calibration,
- and a few more targeted deep fills,
before deciding `V2` vs `V3`.

---

## Best next deep-fill candidates from Batch 3

If we want the next manual case fills to produce the most leverage, the best candidates are:

1. `2025-06-21 / Virginia4 / Midday / 473`
- best control for stress-testing `dr_empty_lens`

2. `2025-12-31 / Delaware4 / Evening / 337`
- strong buried-trace positive from another window

3. `2025-12-31 / NewYork4 / Evening / 116`
- best “false active” control challenge

4. `2026-01-03 / Florida4 / Evening / 611`
- good double-trace case where the double surface is present but not dominant

5. `2025-06-23 / Indiana4 / Midday / 110`
- older-window positive with strong exact trace and cleaner positive/control contrast

---

## Broad-screen conclusion

The broader screen strengthens three conclusions:

1. the main positive DR arena surfaces are real,
2. `dr_empty_lens` is the main weak point,
3. we still do **not** need to retune DR or redesign the analyzer yet.

The next best move is:
- a small number of targeted deep fills from Batch 3,
- then `DR Arena v1.1` style calibration on sparse-control logic,
- then the first real DR consumer-side change.
