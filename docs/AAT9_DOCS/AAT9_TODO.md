<!-- aat9 -->
For open tasks see TODO.md and CHANGELOG.md in the repo root.

# TODO.md  (📅 last updated 2025-07-02)

## Extractor (v1.0.0 tagged)
### ▲ 2025-07-02 – notes
- Repo green after test clean-up
- Stable extractor v1.0.0 pushed & tagged
- Auto-save CSV confirmed
- Next up: Digit-Reducer design
- [x] ✅ Archive legacy copies
- [x] ✅ 3-value V-Trac fix
- [x] ✅ single_left == 3 rows
- [x] ✅ hot-zone decay
- [x] ✅ straight tie-break bias
- [ ] 🔒 No open items (frozen 👑)
- Auto-save filename now includes state and lands in data/outputs/patterns/
- Legacy auto-save to analysis/patterns disabled

## Digit Reducer
- [ ] Design V-Trac+pairing rules  (📅 added 2025-06-27)
- [ ] Prototype score weights
- [ ] Unit tests
- [ ] 🟡 Part 1/2 wired to UI; implement Part 3 tally next

## General v0 (repetition detector)
- [ ] Build SQLite ingest script
- [ ] Streamlit report "Yesterday + Today repeats" 

<!-- aat9 -->
For open tasks see TODO.md and CHANGELOG.md in the repo root.

# AAT9 — Rolling TODO / Road‑map

Legend 🟢 planned 🟡 in‑progress 🔴 blocked

| Epic | Sub‑task | Status | Notes |
|------|----------|--------|-------|
| **Digit Reduction** | Port Part 3 "tally & rank" | 🟡 | Most algorithms exist; needs wrapper + tests. |
| | Wire Streamlit tab | 🟢 | Mirror pattern‑extractor pattern. |
| **Hot‑Zone** | Compute engine | 🟢 | Re‑use consensus logic blueprint. |
| | Report builder | 🟢 | HTML first, Streamlit later. |
| **Winner Logging** | Unify JSON schema | 🟢 | Decide single payload (`draw_date`, `tool`, `hit_flag`, …). |
| | Hook into V‑Trac & Stable‑Pattern runs | 🟢 | Write once per state/day. |
| **Brain (Analysis)** | Feature catalog (.yaml) | 🟢 | One row per feature; owner/tool/ref. |
| | Baseline scorer (rule weights) | 🟢 | Use 2023‑2024 history for first fit. |
| **Dev Experience** | `make clean‑artefacts` | 🟢 | Purge outputs locally. |
| | Pre‑commit black+ruff | 🟢 | Keep style consistent. |