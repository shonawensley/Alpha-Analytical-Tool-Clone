# AAT9 Changelog

## Unreleased
- [ ] Move code into `src/` package
- [ ] Hot-Zones stub (`src/core/hot_zones.py`) returns `{}`
- [ ] Wire Digit-Reduction Part 3 after Analysis module arrives
- [ ] Minor fixes (see `docs/AAT9_Minor_Fixes_Checkpoint_v0.3.md`)

## v0.3-checkpoint (2025-06-06)
### Added
- V-TRAC module → **3-prediction + bundle JSON** output
- `utils/bundler.py`
- Docs: V-TRAC Enhancement guide + Minor Fixes list
### Fixed
- `streamlit_app_with_analyzer.py` NameError (`script_dir`) + bundle writer
### Deferred
- Digit-Reduction Part 3 (parked)
<!-- aat9 -->
For open tasks see TODO.md and CHANGELOG.md in the repo root.

## [2025‑06‑29] Stable‑Pattern Extractor consolidation
* Switched Streamlit + batch paths to `core.module_a_stable_patterns`.
* Auto‑save now drops **both** HTML & CSV into `data/outputs/analysis/patterns/<STATE>/`.
* Removed legacy extractor code and flaky test import.
* Minor UI polish (R2‑only labels) + dependency clean‑up.