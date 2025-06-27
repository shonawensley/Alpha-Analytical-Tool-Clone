<!-- aat9 -->
For open tasks see TODO.md and CHANGELOG.md in the repo root.

## [1.0.0] – 2025-06-27
### Added
- Frozen Stable-Pattern Extractor tagged v1.0.0 and moved to `alpha_analytical.stable`.
- Hot-zone decay, single_left strict rule, 3-value V-Trac check, straight tie-break adjustment.
- Auto-save CSV in Streamlit stable-pattern tab.
- Unit tests for critical rules (`tests/test_rules.py`).

### Changed
- Import wrapper now targets stable package.

### Removed
- Legacy `stable_pattern_analyzer_standalone.py` archived. 