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
- `OntarioCanada4`: Fix-later: DR Evening overlay for Ontario 616 is a 0-match negative-control (items_total=0); do not treat as missing artifacts.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__OntarioCanada4.md`
- `PuertoRico4`: Fix-later: decide whether PR “missing results days” should be skipped automatically in report generation (to reduce confusion).
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__PuertoRico4.md`
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

## D=2025-12-30

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__Virginia4.md`

## D=2025-12-31

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__Virginia4.md`

## D=2026-01-01

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__Virginia4.md`

## D=2026-01-02

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__Virginia4.md`

## D=2026-01-03

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__Virginia4.md`

## D=2026-01-04

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__Virginia4.md`

## D=2026-01-05

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05__Virginia4.md`

## D=2026-01-06

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__Virginia4.md`

## D=2026-01-07

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Virginia4.md`

## D=2026-01-08

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__Virginia4.md`

## D=2026-01-09

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__Virginia4.md`

## D=2026-01-15

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__Virginia4.md`

## D=2026-01-16

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Virginia4.md`

## D=2026-01-17

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-17__Virginia4.md`

## D=2026-01-18

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-18__Virginia4.md`

## D=2026-01-20

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-20__Virginia4.md`

## D=2026-01-21

- `Connecticut4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Connecticut4.md`
- `Delaware4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Delaware4.md`
- `Florida4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Florida4.md`
- `Indiana4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Indiana4.md`
- `Michigan4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Michigan4.md`
- `NewJersey4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__NewJersey4.md`
- `NewYork4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__NewYork4.md`
- `NorthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__NorthCarolina4.md`
- `Ohio4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Ohio4.md`
- `OntarioCanada4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__OntarioCanada4.md`
- `Pennsylvania4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Pennsylvania4.md`
- `PuertoRico4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__PuertoRico4.md`
- `SouthCarolina4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__SouthCarolina4.md`
- `Virginia4`: Fix-later: tune gates/decays only after larger corpus; consider mirror-double/VTRAC-family closure as a pack-builder rule.
  - Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-21__Virginia4.md`
