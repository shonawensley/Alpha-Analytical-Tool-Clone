# Alpha Analytical Tool 9 (AAT9)

> Banner: For the curated, up‑to‑date AAT9 documentation and workflow, see `docs/AAT9_KIT/AAT9_KIT_README.md`. Older AAT9 docs remain for history and reference.

Welcome to **AAT9**, a modularized analytics suite for lottery pattern extraction, digit reduction, hot zone analysis, and final synergy aggregation. This documentation set is specifically for **AAT9**, distinguishing it from any older docs or prototypes in the repository.

## Canonical Setup (AAT9)
- Launch the integrated app via `run_app.bat` → `streamlit run src\app.py` (from repo root).
- Imports resolve to in-repo files: `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`.
- Data contracts:
  - Aux/Blackapple → `data/cleaned/*_draws.csv` (draws only)
  - V‑TRAC / Stable / Digit Reduction → combined tables under `tables/` or `data/outputs/tables/<STATE>/` (via `utils.path_handler`).
- Preflight (recommended): `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"` to print cwd, Python, module sources, and draws inventory.
- Reference: see `AAT9_Architecture_Dir_Layout_2025-09-06.md` for the canonical directory tree and diagrams.

## What Is AAT9?

AAT9 is our **latest, streamlined** approach to:

1. **Generate** standard CSV tables for each state (Midday/Evening/Combined).
2. **Analyze** stable patterns (Module A).
3. **Uncover** hidden combos via digit-reduction (Module B).
4. **Identify** short-late or star-labeled "Hot Zones" (Module C).
5. **Aggregate** or unify all findings with synergy logic (Module D).

It builds upon prior attempts yet stays separate and "clean," allowing us to reference older docs/code if needed without overwriting them.

## Quickstart

1. **Generate CSV Tables**  
   - Run `generate_tables_pipeline.bat` to produce `data/outputs/tables/STATE/...`.
2. **Run Module A** (Stable Extractor)  
   - `python stable_pattern_extractor.py --state=Florida4 --output=stable_patterns.json`
3. **Run Module B** (Digit Reduction)  
   - `python digit_reduction.py --state=Florida4 --output=longstring_patterns.json`
4. **Run Module C** (Hot Zones)  
   - `python hot_zones.py --state=Florida4 --output=hotzone_patterns.json`
5. **Aggregator** (Module D)  
   - `python aggregator.py --stable stable_patterns.json --digit longstring_patterns.json --hot hotzone_patterns.json --output aggregator_synergy.json`

Review the synergy JSON or final user interface to see top patterns.

## Documentation Structure (AAT9)

- **modules/**  
  - [Module A – Stable Pattern Extractor](modules/module_A_stable_extractor.md)  
  - [Module B – Digit Reduction](modules/module_B_digit_reduction.md)  
  - [Module C – Hot Zones](modules/module_C_hot_zones.md)
  - [Module D – V-TRAC Analyzer](modules/AAT9_Module_VTRAC_Enhancement.md)
  - [Module E – Aggregator](modules/module_D_aggregator.md)
- **architecture_AAT9.md**  
  - Overarching system flow / diagram for AAT9
- **data_formats_AAT9.md**  
  - Explains standard CSV tables, JSON exports, etc.
- **ML_NOTES_AAT9.md**  
  - Parking-lot ideas for machine learning expansions
- **any_other_docs** you'd like for versioning.

## Relation to Old Docs

We keep older docs for reference. They might be named `README_legacy.md`, `old_process_docs/`, etc. **AAT9** doesn't conflict with them; we simply treat those as historical. This ensures no confusion while we keep a clear path forward. 
