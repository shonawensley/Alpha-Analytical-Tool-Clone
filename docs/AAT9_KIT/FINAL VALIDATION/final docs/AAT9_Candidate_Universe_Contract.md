# Candidate Universe / Playset Contract (Pre‑Results, Gradeable)

Purpose: define the **one** artifact that makes predictive performance measurable.

- Master Validation run reports/templates are **evidence + reasoning**.
- The Candidate Universe / Playset is the **explicit, pre‑results predictions feed** that can later be graded honestly.

This contract exists to prevent:
- **time contamination** (anything winners‑dependent leaking into pre‑results snapshots),
- terminology drift (“mirror” ambiguity, “VTRAC” ambiguity),
- and non‑deterministic prediction artifacts.

---

## Definitions (date mapping)

- **H** = history workbook date (Pick3StatsC4 history workbook)
- **D** = results date (**D = H + 1 day**)

Snapshot roots:
- **Predictive (“before”)**: `sharepacks/_predictive/<D>/...` (no results/winners yet)
- **Post‑results (“after”)**: `sharepacks/<D>/...` (winners lens + evaluation allowed)

---

## Non‑negotiables

1) Candidate Universe artifacts for a predictive day are generated **only from sharepack‑local evidence** (read‑only inputs).
2) Predictive packs must remain **winners‑free**:
   - no `winners/` folders,
   - no winners‑dependent VTRAC validation artifacts (`validation_report.*`),
   - no Profit Alerts evaluation artifacts (`profit_alerts_eval.*`).
3) Default mirror scheme is **VTRAC‑pair** (difference‑5 pairing), not “sum‑to‑9”:
   - `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`
4) “VTRAC” must be disambiguated in artifacts:
   - `vtrac_index` = boxed family index (`get_vtrac_index`)
   - `vstraight_lane` / `vstraight_vcode` = positional 8‑combo lane (VSTRAIGHTS / STR8_8 semantics)

---

## Output locations (SSOT contract)

Per state/day (predictive “before” snapshot):
- Candidate Universe is **profiled** (Profit Alerts quarantine is expressed via `--profile`).
- Files follow the convention: `candidate_universe{__profile}.json` where `__profile` is omitted for `mixed`.
- Current default generation posture is `tool_only`, so the default filename is suffix-named.

Profiled outputs (common cases):
- Default (recommended; Profit Alerts excluded): `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
- Mixed (includes Profit Alerts): `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json` (`--profile mixed`)
- Profit only (Profit Alerts only): `sharepacks/_predictive/<D>/<STATE>/candidate_universe__profit_only.json` (`--profile profit_only`)
- Optional human view (if `--write-md`): `candidate_universe{__profile}.md`

Post‑results grading outputs (do **not** write into predictive sharepacks):
- Grading is also **profiled** and follows the convention: `<D>__CANDIDATE_UNIVERSE_GRADE{__profile}.*` where `__profile` is omitted for `mixed`.
- Default (recommended; tool-first): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE__tool_only.csv` and `.md`
- Mixed (includes Profit Alerts): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.csv` and `.md` (`--profile mixed`)

---

## Schema (minimum required fields)

The JSON file is a single object with:

- `schema_version` (string)
- `generated_at` (ISO timestamp)
- `results_date` (D, `YYYY-MM-DD`)
- `history_date` (H, `YYYY-MM-DD` if available)
- `state_key` (e.g., `NewJersey4`)
- `sharepack_root` (e.g., `sharepacks/_predictive`)
- `sharepack_state_dir` (path string)

Terminology locks:
- `mirror_scheme` = `"vtrac_pair"`

Anti‑leakage:
- `contains_winners_artifacts` = `false`
- `leakage_checks` = list of strings describing what was checked

Determinism:
- `inputs` = list of sharepack‑relative evidence paths used
- `inputs_hash` = hash of `(path + size + content)` across `inputs`

Core predictive content:
- `digit_envelopes` (list; may be empty)
  - Each envelope includes:
    - `digits` (list of `"0".."9"`)
    - `sources` (list of strings; tool+path provenance)
    - `derived_triads` (list of triads derived from the envelope)
    - `notes` (optional strings)
- `packs` (list)
  - Each pack includes (minimum):
    - `pack_id` (unique within state/day)
    - `method_id` (string; e.g. `profit_alerts`, `PackA_vt8`, `PackB_mirror3rd`)
    - `variant` (`Combined|Midday|Evening|Unknown`)
    - `play_mode` (`BOX|STRAIGHT|MIXED`)
    - `canonicals` (list of 3‑digit canonicals; may be empty)
    - `combos` (list of 3‑digit straight combos to play)
    - `combos_count` (int)
    - `cost_units` (int; default equals `combos_count`)
    - `why_tags` (list of short tags; tool/logic cues)
    - `transform_chain` (list; required for attribution)
    - `evidence_paths` (list of sharepack‑relative file paths)

Union convenience:
- `union_combos` (sorted unique list of all combos across packs)
- `union_combos_count` (int)

---

## Generation (workflow)

Predictive day build:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`

Generate Candidate Universe (tooling only; no analyzer runs):
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive
```

Grade once results exist (writes only to RUNS):
```bash
python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive
```

---

## Notes (why this exists)

- A “pack covers winner” statement inside a post‑results sharepack is **not** predictive performance.
- Predictive performance requires:
  - an immutable “before” snapshot (`sharepacks/_predictive/<D>/...`)
  - a deterministic, sharepack‑local Candidate Universe artifact
  - grading that happens later, outside the predictive snapshot
