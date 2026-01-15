# CODEX HANDOFF — Aux Audit + Candidate Universe (Due Doubles)

Repo root (WSL canonical): `/home/ser/code/Alpha-Analytical-Tool-Clone`

Purpose:
- Capture what was validated/changed around Aux + Candidate Universe so a new chat can resume in minutes.
- Keep predictive packs (`sharepacks/_predictive/<D>/`) winners‑free and gradeable.

## What changed (high signal)

### 1) Aux “what are we actually capturing?” (legend + gap closure)
- New SSOT doc explaining Aux coverage and the Due Doubles board semantics:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Aux_Coverage_And_Legend.md`
- Key clarification: the Control Center Due Doubles board is grouped by **VTRAC double families** (e.g. `0/5-1/6`), not `vtrac_index` (1–35).

### 2) Candidate Universe now includes Due Doubles (gradeable)
- Updated `scripts/tools/create_candidate_universe.py` to parse:
  - `sharepacks/<ROOT>/<D>/control_center/due_doubles.csv`
- It emits bounded BOX packs:
  - `due_doubles:<Variant>` (Combined/Midday/Evening) per state, default `top_n=4` canonicals ⇒ ~12 combos (box perms).
- CLI knob:
  - `--top-n-due-doubles <N>`
- Optional bounded mirror-double expansions are also supported (seeded from the top due-doubles canonical):
  - `--due-doubles-mirror-seeds <N>` (default: 1; set `0` to disable)
  - Packs: `due_doubles_mirror_single:*` and `due_doubles_mirror_double:*`

### 3) Regenerated artifacts (D=2026-01-07)
- Wrote Candidate Universe for all tracked states:
  - `sharepacks/_predictive/2026-01-07/<STATE>/candidate_universe.json`
- Re-graded against results (writes only to RUNS):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__CANDIDATE_UNIVERSE_GRADE.csv`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__CANDIDATE_UNIVERSE_GRADE.md`
- Generated predictive run report scaffolds (human notes):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__<STATE>__PREDICTIVE.md`
- Generated a cross-state predictive portfolio triage report (fast “where to focus”):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__PREDICTIVE_PORTFOLIO.md`

### 4) Small hygiene
- Deleted a tracked empty placeholder file:
  - `docs/AAT9_KIT/FINAL VALIDATION/New Text Document.txt`
- Linked the Aux legend from the Final Docs portal:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`

## Commands (repeatable)

Generate Candidate Universe (predictive “before”):
```bash
python3 scripts/tools/create_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive --force
```

Generate a cross-state predictive portfolio report:
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive --force
```

Grade once results exist (writes only to RUNS):
```bash
python3 scripts/tools/grade_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive --force
```

## Fix-later (explicitly deferred)
- Horizon / carryover grading (N-draw window scoring) — keep as a backlog item until the baseline corpus is stable.
- Optional “boxed VTRAC combo symbol table” export (all combos in each `vtrac_index` with pair/positional badges) if we decide it’s worth the extra reporting surface.
