# Translator Redesign Lessons From Evidence Utilization Audit

This memo converts the March audit into design guidance for a future Analysis Arena-native candidate translator.

## 1. Main Finding

- The primary redesign target is not more broad evidence capture; it is cleaner promotion from evidence into separated boxed, straight, VTRAC, and decay lanes.
- Captured-and-used: `23`; captured-but-underused: `2`; wrong-lane: `15`.
- Box/exact gaps: `2`; VTRAC-only: `35`.

## 2. Candidate Lane Implications

- Boxed lane should prioritize exact/box-aligned Arena, sandbox, play-card, profit-alert, double-anchor, family-frontier, and box-gap evidence.
- Straight lane should remain stricter: exact sandbox, exact play-card, literal frontier, positional combo exactness, and direct profit-alert evidence should carry more weight than broad canonical context.
- VTRAC lane should be treated as territory/carryforward unless paired with box/exact evidence or a strong frontier/double signal.
- Decay lane should remain separate from same-day grading but feed carryforward watch decisions.

## 3. Signals Worth Promoting Into Future Scoring Experiments

- `play_card_any_box`: present `5`, converted `5`, gap `0`; Conversion-grade candidate signal in this window.
- `sandbox_exact_seed`: present `1`, converted `1`, gap `0`; Conversion-grade candidate signal in this window.
- `arena_exact_signal`: present `1`, converted `1`, gap `0`; Conversion-grade candidate signal in this window.
- `play_card_any_exact`: present `13`, converted `12`, gap `1`; Conversion-grade candidate signal in this window.
- `sandbox_box_seed`: present `3`, converted `2`, gap `1`; Conversion-grade candidate signal in this window.
- `arena_box_signal`: present `4`, converted `2`, gap `2`; High-priority translator-learning signal; often saw value that old final layer missed.
- `arena_primary_box`: present `3`, converted `1`, gap `2`; High-priority translator-learning signal; often saw value that old final layer missed.

## 4. Source Rows Worth Preserving For Brain1/Brain2 Training

- `translation_sandbox:diagnostic_straight_seed`: pre-draw aligned `67`, exact `2`, box `9`, VTRAC `66`.
- `old_candidate_universe:pack:stable_top`: pre-draw aligned `51`, exact `0`, box `6`, VTRAC `51`.
- `old_play_card:ranked_candidate_canonical`: pre-draw aligned `51`, exact `0`, box `6`, VTRAC `51`.
- `old_play_card:ranked_candidate_combo`: pre-draw aligned `51`, exact `1`, box `6`, VTRAC `51`.
- `translation_sandbox:diagnostic_boxed_seed`: pre-draw aligned `45`, exact `0`, box `6`, VTRAC `42`.
- `old_play_card:budgeted_canonicals_top`: pre-draw aligned `39`, exact `0`, box `5`, VTRAC `39`.
- `positional:positional_canonical`: pre-draw aligned `33`, exact `0`, box `4`, VTRAC `33`.
- `positional:positional_combo`: pre-draw aligned `33`, exact `0`, box `4`, VTRAC `33`.
- `brain1:secondary_canonicals`: pre-draw aligned `33`, exact `0`, box `1`, VTRAC `33`.
- `brain1:dominant_canonicals`: pre-draw aligned `30`, exact `0`, box `3`, VTRAC `30`.
- `translation_sandbox:diagnostic_vt_box_seed`: pre-draw aligned `30`, exact `0`, box `0`, VTRAC `30`.
- `old_candidate_universe:pack:due_doubles`: pre-draw aligned `27`, exact `0`, box `0`, VTRAC `27`.

## 5. Guardrails

- Do not build one master score yet; first add exposure/false-positive denominators for source keys.
- Keep Brain2 rank diagnostics active because static rank can make top-primary metrics look stronger than they are.
- Keep bonus/fireball sidecar separate from standard boxed/straight metrics.
- Use this audit to choose fixtures for future translator tests before rewriting candidate generation.
