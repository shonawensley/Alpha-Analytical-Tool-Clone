# VTRAC Enhanced — v0 Audit (Cases)

Purpose: pick a small number of **high-signal VTRAC cases** to understand:
- why VTRAC Enhanced top‑N straights often miss as a direct caller, and
- how often VTRAC Enhanced is “right about the index” (lane hit) even when it misses the canonical/straight.

Scope guardrails:
- No analyzer changes (Stable/DR/VTRAC/HZ).
- Profit Alerts quarantined (use `--profile tool_only` as baseline).

Companion quant:
- v0 audit narrative: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
- harness outputs (case selection SSOT):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-06-21_to_2025-06-23.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-12-30_to_2026-01-04.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2026-01-05_to_2026-01-09.md`

Winner type note:
- **Doubles are included** in `vtrac_index` metrics (indices 1–35).
- **Triples intentionally have no** `vtrac_index` (legacy behavior; `modules.vtrac_reference.get_vtrac_index()` returns `None`).

---

## How to review one case (repeatable checklist)

For each case below:
1) Winners lens (environment truth):
   - `sharepacks/<D>/<STATE>/winners/<STATE>/*.html` (+ `.json` twin if present)
2) Master Validation run report (structured extraction of tool evidence):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
3) VTRAC Enhanced bundle (the thing we measure):
   - `sharepacks/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`
4) VTRAC sharepack summary (if present; index placement / context):
   - `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json`
5) Predictive artifacts (optional, when available; before→after comparison):
   - `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
   - `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only.json`
6) Winners digest (optional quick scan):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`

Key questions:
- Did the winner’s **index** place high even when the winner’s literal straight didn’t?
- Is this an “index-hit → box-miss” case (convertible via bounded closure), or just noise?
- Would BOX-equivalent canonicalization of the top straights have converted this?

---

## Harness-selected case pool (three regression windows)

Definitions used below (from the harness CSVs):
- **Direct hit**: `straight_hit_top8=1`
- **Canonical-only hit**: `canonical_hit_top8=1` and `straight_hit_top8=0`
- **Index-hit-only queue**: `index_hit_top12=1` while `canonical_hit_top12=0` and `straight_hit_top12=0`

### Window: 2025-06-21 → 2025-06-23

**Direct hits (top‑8)**: _none_

**Canonical-only hits (top‑8)**
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2025-06-21|Connecticut4|Midday|950|059|unique|5|
|2025-06-23|NorthCarolina4|Evening|145|145|unique|9|
|2025-06-23|Ohio4|Evening|368|368|unique|23|
|2025-06-23|SouthCarolina4|Evening|314|134|unique|24|

**Index-hit-only queue (top‑12)** (first 12; see harness CSV for full list)
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2025-06-21|NewJersey4|Midday|182|128|unique|21|
|2025-06-21|Ohio4|Midday|069|069|unique|9|
|2025-06-21|OntarioCanada4|Midday|678|678|unique|21|
|2025-06-21|SouthCarolina4|Midday|069|069|unique|9|
|2025-06-22|Florida4|Midday|330|033|double|13|
|2025-06-22|NewYork4|Evening|968|689|unique|24|
|2025-06-23|Florida4|Evening|465|456|unique|9|
|2025-06-23|Florida4|Midday|665|566|double|6|
|2025-06-23|Michigan4|Midday|392|239|unique|30|
|2025-06-23|SouthCarolina4|Midday|958|589|unique|14|
|2025-06-23|Virginia4|Midday|579|579|unique|12|

### Window: 2025-12-30 → 2026-01-04

**Direct hits (top‑8)**
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2026-01-01|NorthCarolina4|Evening|053|035|unique|4|
|2026-01-04|Indiana4|Midday|813|138|unique|23|

**Canonical-only hits (top‑8)**
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2025-12-30|Connecticut4|Midday|095|059|unique|5|
|2026-01-01|Delaware4|Midday|149|149|unique|25|
|2026-01-02|OntarioCanada4|Evening|816|168|unique|18|
|2026-01-03|SouthCarolina4|Midday|189|189|unique|24|

**Index-hit-only queue (top‑12)** (first 12; see harness CSV for full list)
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2025-12-30|Delaware4|Evening|563|356|unique|8|
|2025-12-30|Indiana4|Evening|512|125|unique|7|
|2025-12-30|NorthCarolina4|Midday|455|455|double|5|
|2025-12-30|PuertoRico4|Evening|643|346|unique|24|
|2025-12-30|PuertoRico4|Midday|098|089|unique|14|
|2025-12-31|NewJersey4|Midday|366|366|double|18|
|2025-12-31|OntarioCanada4|Evening|932|239|unique|30|
|2025-12-31|PuertoRico4|Evening|913|139|unique|24|
|2025-12-31|SouthCarolina4|Midday|653|356|unique|8|
|2025-12-31|Virginia4|Evening|636|366|double|18|
|2025-12-31|Virginia4|Midday|686|668|double|18|
|2026-01-02|NorthCarolina4|Midday|033|033|double|13|

### Window: 2026-01-05 → 2026-01-09

**Direct hits (top‑8)**
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2026-01-07|Florida4|Evening|963|369|unique|24|

**Canonical-only hits (top‑8)**
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2026-01-08|Delaware4|Evening|031|013|unique|8|

**Index-hit-only queue (top‑12)** (first 12; see harness CSV for full list)
|results_date|state|outcome|winner|winner_canonical|winner_kind|winner_index|
|---|---|---|---|---|---|---|
|2026-01-05|OntarioCanada4|Evening|797|779|double|28|
|2026-01-05|Pennsylvania4|Evening|600|006|double|2|
|2026-01-05|SouthCarolina4|Evening|712|127|unique|20|
|2026-01-06|NewJersey4|Midday|865|568|unique|8|
|2026-01-06|SouthCarolina4|Evening|412|124|unique|22|
|2026-01-06|Virginia4|Evening|958|589|unique|14|
|2026-01-07|Florida4|Midday|434|344|double|34|
|2026-01-07|Indiana4|Evening|290|029|unique|12|
|2026-01-07|Ohio4|Evening|204|024|unique|12|
|2026-01-07|Pennsylvania4|Evening|263|236|unique|21|
|2026-01-08|SouthCarolina4|Evening|910|019|unique|9|
|2026-01-08|Virginia4|Midday|286|268|unique|21|
