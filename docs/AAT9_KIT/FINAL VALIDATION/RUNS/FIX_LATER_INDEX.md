# Fix-Later Index (from Run Reports)

This is an auto-extracted index of `Fix-later` notes from filled run reports.

Source folder: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

## D=2025-06-21

- `Connecticut4`: Fix-later: consider a rule for “dominant family but low triple rank” days (cheap box probes vs skip).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Connecticut4.md`
- `Delaware4`: Fix-later: decide how to treat “Stable exact but extremely low rank” days (skip vs minimal hedge).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Delaware4.md`
- `Florida4`: Fix-later: | Add an explicit “near-lane adjacency” hypothesis test (e.g., Hot Zones top lane `278` → box `278` and optionally `279` when lane pressure is extreme). | Tighten “candidate universe” inclusion rules (require ≥2 evidence vectors) to reduce noisy box sets.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Florida4.md`
- `Indiana4`: Fix-later: investigate whether Evening “winner not surfaced” cases correlate with specific table conditions or require different lane definitions.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Indiana4.md`
- `Michigan4`: Fix-later: test whether “Combined lens dominance” is a repeatable trait for Michigan and whether it correlates with specific Aux digit themes.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Michigan4.md`
- `NewJersey4`: Fix-later: formalize a “dominant-lane miss” capture rule (log when Stable+VTRAC+HZ agree strongly but winners land elsewhere) and ensure cross-variant evaluation is always included for these days.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewJersey4.md`
- `NewYork4`: Fix-later: | Add a “consensus cluster miss” tag to aggregator memory so strong clusters are not over-weighted after one day. | Track “Aux index due vs Brain VTRAC rank” disagreements over more days to decide which should drive VT-family packs.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewYork4.md`
- `NorthCarolina4`: Fix-later: formalize how to act when HZ+BA agree but Stable/VTRAC disagree (cheap hedge tier), and log “Combined-only sparse winners” as their own environment class.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NorthCarolina4.md`
- `Ohio4`: Fix-later: log this as a “positive control” case for future superbrain tuning (what strong convergence looks like).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Ohio4.md`
- `OntarioCanada4`: Fix-later (aggregator hypotheses): | Combine Hot Zones Top lanes ∩ Winners-lens dominant survivors (e.g., 367) as a candidate reducer before spending. | Add a “dominant survivor boost” concept to VTRAC analyzer index ranking (log-only; do not change code yet). | Use DR as a digit/value constraint layer to reduce candidate space (not as a direct predictor).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: consider explicit logic for “due double canonical” as an overlay that can rescue a low-ranked stable/hz candidate.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: investigate DR Combined winner stamp being 221 for PuertoRico4 on 2025-06-21; log outcome as workflow hygiene.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: treat this as a negative-control “no greenlight” case when designing gating thresholds.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__SouthCarolina4.md`
- `Virginia4`: Fix-later: investigate DR Midday overlay emptiness for VA; consider adding explicit “pass day” gating rules to the aggregator.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Virginia4.md`

## D=2025-06-22

- `Connecticut4`: Fix-later: keep as a negative-control case for aggregator gating (“high heat but wrong lane”).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Connecticut4.md`
- `Delaware4`: Fix-later: treat as a “dominant-lane miss” day in corpus analysis; track whether Aux overdue membership is a useful cheap hedge trigger.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Delaware4.md`
- `Florida4`: Fix-later (tuning / aggregator hypotheses): | Add an explicit “Aux overdue index rescue” rule: allow index coverage when Aux overlay is strong even if VTRAC Analyzer rank is low. | Add a “col1 ladder dominance is environment-classification, not direct prediction” note to aggregator guidance.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Florida4.md`
- `Indiana4`: Fix-later: corpus-based calibration for “when dominant-lane agreement is misleading” and whether Stable exact-hit ranks can be promoted without overfitting.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Indiana4.md`
- `Michigan4`: Fix-later: quantify “Stable exact hit + low rank strength” days vs “Stable rank‑top with corroboration” days (to tune confidence tiers without overfitting).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Michigan4.md`
- `NewJersey4`: Fix-later: quantify “deep-ranked exact hits” vs “top-tier convergence hits” to tune confidence tiers without overfitting.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewJersey4.md`
- `NewYork4`: Fix-later: define/quantify “skip day” heuristics (when Stable+DR+Aux agree on a dominant universe that is orthogonal to winners).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewYork4.md`
- `NorthCarolina4`: Fix-later: quantify when “Combined-lens on-board” should override weak draw-specific ladder evidence.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NorthCarolina4.md`
- `Ohio4`: Fix-later: investigate why Combined Set1 col1 winners-lens lane string becomes `nan**` for Ohio4 (winners generator hygiene).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Ohio4.md`
- `OntarioCanada4`: Fix-later: DR Evening overlay missing flags/hits for Ontario (winner 616).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: DR Combined winner mapping (shows 925, date=None) likely pulling the wrong state’s result.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: decide whether PR “missing results days” should be skipped automatically in report generation (to reduce confusion).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: handle one-winner days cleanly (South Carolina Midday blank): | Stable/Hot Zones summaries label “Midday winner 675” even though it’s the Evening outcome. | DR produces “Evening winner unknown” + missing Evening stamp/flags/hits; should be skipped/treated as expected when Midday is blank.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__SouthCarolina4.md`
- `Virginia4`: Fix-later: none specific (avoid tuning; collect more examples).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Virginia4.md`

## D=2025-06-23

- `Connecticut4`: Fix-later: none specific (avoid tuning; collect more examples).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Connecticut4.md`
- `Delaware4`: Fix-later: none (avoid tuning; collect more examples).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Delaware4.md`
- `Florida4`: Fix-later: none (avoid tuning; collect more examples).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Florida4.md`
- `Indiana4`: Fix-later: none (collect more examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Indiana4.md`
- `Michigan4`: Fix-later: none (collect more examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Michigan4.md`
- `NewJersey4`: Fix-later: none (collect more examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewJersey4.md`
- `NewYork4`: Fix-later: none (collect more examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewYork4.md`
- `NorthCarolina4`: Fix-later: none (collect more examples of “exact-but-deep” Midday outcomes before tuning weights).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NorthCarolina4.md`
- `Ohio4`: Fix-later: none (collect more split-channel examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Ohio4.md`
- `OntarioCanada4`: Fix-later: none (collect more Ontario examples before tuning).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: none (this day should be treated as a “channel split” example in later synthesis).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: DR Combined winner uses 551 for this state/date; investigate why Combined is not using the Midday winner (template filling can proceed regardless).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__PuertoRico4.md`
