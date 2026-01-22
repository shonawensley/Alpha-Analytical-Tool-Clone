# ChatGPT Pro — Deep Research Prompt (Play Cards + Budgets + Combo Packs)

## Mission

Evaluate the system’s “budget / combinations / play cards” design and identify:
- what the system is currently optimizing for (explicit + implicit),
- where selection/grading semantics may mismatch the project’s training intent (lane visibility vs conversion),
- and the smallest high-leverage improvements that preserve safety (no analyzer edits, predictive-safe).

Important constraints:
- Do not suggest editing core analyzers (Stable/DR/VTRAC/HZ) unless there is a contract violation.
- Treat `sharepacks/_predictive/<D>/...` as winners-free evidence snapshots.
- Grading outputs belong in RUNS, not sharepacks.

## Read first (strict order)

1) Navigation + why these layers exist:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

2) Contracts / semantics:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`

3) Core code (selection):
- `scripts/tools/create_candidate_universe.py`
- `scripts/tools/create_play_card.py`
- `scripts/tools/create_predictive_portfolio_report.py`
- `scripts/tools/run_v0_3_cycle.py`

4) Core code (grading + rollups):
- `scripts/tools/grade_candidate_universe.py`
- `scripts/tools/grade_play_card.py`
- `scripts/tools/grade_play_card_windowed.py`
- `scripts/tools/rollup_candidate_universe_corpus.py`
- `scripts/tools/rollup_play_card_corpus.py`

5) VTRAC reference anchor (boxed packs vs straight expansion):
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

## Deliverables

1) **Plain-English architecture**
- Explain how Candidate Universe → Play Cards → grading/rollups work, and where budgets influence outcomes.

2) **Semantics audit**
- Confirm (or critique) the current hit metrics naming/meaning:
  - lane visibility vs boxed closure vs straight conversion vs inclusive hit.
- Identify any terminology/metric naming that could mislead users.

3) **Selection policy review**
- Is the current default posture (B12 conservative, B24/B36 conversion-friendly) well-justified?
- If not, propose an alternative with explicit acceptance criteria and guardrails.

4) **Top 5 risks**
- List the top 5 failure modes where budgets/strategies could unintentionally hide tool value (e.g., over-penalizing “right lane”).

5) **Two minimal improvements**
- Two small, safe improvements that would most increase clarity + measurement quality (not “add more candidates”).

