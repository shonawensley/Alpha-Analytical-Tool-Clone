# Digit Reduction — Envelope Harness (v0) — Analysis Notes

Purpose: interpret the DR envelope harness outputs as a **measurement bridge** between DR’s trace evidence (`*_digit_reduction_steps.csv`) and the “gateway language” we use elsewhere (canonical vs `vtrac_index`).

This is not an analyzer-tuning proposal. It is an interpretation of what the harness already shows, and what it implies for v0.2/v0.3.

Primary references:
- Harness outputs:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-06-21_to_2025-06-23.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2025-12-30_to_2026-01-04.md` (and `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
- DR posture decisions:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
- Case selection surface:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md`

---

## 1) What the harness is (and isn’t)

It evaluates DR as an **envelope/digit-pool** evidence source by:
- Reading only `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`.
- Deriving a ranked set of candidate canonicals from digit pools with simple scoring knobs.
- Grading against official results using:
  - canonical Top‑K hit rates (`canon@8/12/20`)
  - `vtrac_index` Top‑K hit rates (`idx@8/12/20`) using `modules.vtrac_reference.get_vtrac_index()`.

It does not:
- Use winners overlays/stamps/hits (anti-leakage).
- Use DR analyzer_v2 “best_pattern” candidates (this harness is explicitly exploring an alternative consumption lens).

---

## 2) High-level finding (consistent across windows)

Across all three regression windows:

- **Canonical Top‑K hit rates remain low** (DR does not behave like a tight “top‑8 caller”).
- **`vtrac_index` Top‑K hit rates are materially higher**, and a meaningful fraction is **index-hit-only** (“rail correct, box miss”).

This matches the qualitative case audits: DR frequently “contains the win” in the trace/overlay, but converting that trace into a tight ranked top list is non-trivial.

Implication:
- v0.2 should continue to treat DR as **evidence**, not as a default caller (`--top-n-dr 0` tool-only).
- v0.3 should focus on DR‑004: a formal envelope extractor that turns trace evidence into **bounded** closure packs.

---

## 3) Knob behavior (what seems robust vs unstable)

The top-performing configs for `idx@12` differ by window, which is a warning against over-tuning weights in-place:

- Step weighting (`step_power=2`) appears frequently in top configs → **early-step emphasis is likely real**.
- Larger digit pools (`max_unique_digits=7/9`) also appear frequently → envelope needs to tolerate larger pools (but must be bounded downstream).
- The “double weight” (`dw`) is **not stable** across windows:
  - some windows prefer stronger double support,
  - others get better index-hit with doubles de-emphasized.

Interpretation:
- We should not “lock weights” into v0.2 based on this harness.
- The harness is better used to:
  - identify **case cohorts** (doubles vs uniques; dense vs sparse trace),
  - and define acceptance thresholds for DR‑004 experiments.

---

## 4) The next correct measurement upgrades

If we want to align DR evaluation to your full “gateway” language:

1) Split results by winner type:
   - 3-unique vs doubles vs triples.
2) Split by variant correctness:
   - Midday vs Evening (and optionally record Combined as a lens only).
3) Add “pool widening” controls:
   - treat `candidates_total` and `avg_box_cost` as first-class regression constraints.

These are measurement-layer changes; they do not require analyzer edits.

---

## 5) Practical “what to do with this” (v0.2/v0.3)

v0.2 (now):
- Keep DR off as a caller by default (`--top-n-dr 0` tool-only).
- Use the study queue + Master Validation + DR overlays to mine bounded “convert this trace into a closure pack” ideas, but keep them as research-only until measured.

v0.3 (next):
- Implement DR‑004 as a deterministic envelope extractor that outputs bounded, gradeable packs.
- Use this harness as the regression gate: raise index-hit and/or reduce index-hit-only without uncontrolled pool widening.

