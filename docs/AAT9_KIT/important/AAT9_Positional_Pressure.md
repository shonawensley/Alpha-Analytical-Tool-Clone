# AAT9 – Positional Pressure Tool (Aux Layer)

Purpose: surface per-position pressure across Combined/Midday/Evening variants while staying draws-only.

## Engine & Data
- Module: `modules/module_d_auxiliary_tools/refactored/positional_tool.py`
- Input: newest-first draws from `data/cleaned/*_draws.csv`
- Outputs per variant:
  - Top-k digits for P1/P2/P3 with gap, score, and tags (mirror, consensus, double pressure, swap)
  - Cross-variant consensus notes and an aggregated positional scorecard
  - Ranked candidate shortlist (optional straight overlay) with tags, digital root, V-TRAC index

## Streamlit Surfaces
- **Auxiliary Tools page**: “Positional Pressure” expander renders Combined/Midday/Evening in parallel (P1/P2/P3 columns, top-3 ranks) using a fixed 360-draw window; hard-due digits are marked in red and the draw source caption remains under each variant.
- **Control Center**: positional heat badge per state/variant (e.g., `P1:7(34) P2:1(21) P3:9(45)`) supports doubles/BA triage.

## Operator Checklist
- Confirm draws via `.codex/preflight.ps1` and Aux Dev Health (draw path + count).
- Use Combined tab as baseline; review Midday/Evening for consensus/mirror reinforcement.
- Read consensus notes and shortlist tags to compound with pairs, sums, BA status.
- Smoke script: `python scripts/checks/smoke_positional.py`.

## Change Log Notes
- Update Quickstart/Workflow when data contracts or surface behaviour changes.
- Log in Unified Changelog + Checkpoint Log for any scoring tweaks or UI placement changes.
