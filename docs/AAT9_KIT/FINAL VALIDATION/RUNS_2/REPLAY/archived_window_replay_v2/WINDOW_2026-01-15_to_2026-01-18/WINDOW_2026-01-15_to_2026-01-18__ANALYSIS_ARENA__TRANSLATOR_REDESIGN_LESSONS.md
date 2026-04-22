# Translator Redesign Lessons From Evidence Utilization Audit

This memo converts the March audit into design guidance for a future Analysis Arena-native candidate translator.

## 1. Main Finding

- The primary redesign target is not more broad evidence capture; it is cleaner promotion from evidence into separated boxed, straight, VTRAC, and decay lanes.
- Captured-and-used: `30`; captured-but-underused: `4`; wrong-lane: `22`.
- Box/exact gaps: `4`; VTRAC-only: `42`.

## 2. Candidate Lane Implications

- Boxed lane should prioritize exact/box-aligned Arena, sandbox, play-card, profit-alert, double-anchor, family-frontier, and box-gap evidence.
- Straight lane should remain stricter: exact sandbox, exact play-card, literal frontier, positional combo exactness, and direct profit-alert evidence should carry more weight than broad canonical context.
- VTRAC lane should be treated as territory/carryforward unless paired with box/exact evidence or a strong frontier/double signal.
- Decay lane should remain separate from same-day grading but feed carryforward watch decisions.

## 3. Signals Worth Promoting Into Future Scoring Experiments

- `play_card_any_box`: present `11`, converted `11`, gap `0`; Conversion-grade candidate signal in this window.
- `sandbox_exact_seed`: present `3`, converted `3`, gap `0`; Conversion-grade candidate signal in this window.
- `arena_exact_signal`: present `3`, converted `3`, gap `0`; Conversion-grade candidate signal in this window.
- `play_card_any_exact`: present `16`, converted `15`, gap `1`; Conversion-grade candidate signal in this window.
- `sandbox_box_seed`: present `10`, converted `8`, gap `2`; Conversion-grade candidate signal in this window.
- `arena_box_signal`: present `12`, converted `8`, gap `4`; Conversion-grade candidate signal in this window.
- `arena_primary_box`: present `9`, converted `5`, gap `4`; High-priority translator-learning signal; often saw value that old final layer missed.

## 4. Source Rows Worth Preserving For Brain1/Brain2 Training

- `old_candidate_universe:pack:stable_top`: pre-draw aligned `91`, exact `0`, box `13`, VTRAC `91`.
- `translation_sandbox:diagnostic_straight_seed`: pre-draw aligned `56`, exact `6`, box `15`, VTRAC `53`.
- `old_play_card:budgeted_canonicals_top`: pre-draw aligned `52`, exact `0`, box `11`, VTRAC `52`.
- `translation_sandbox:diagnostic_boxed_seed`: pre-draw aligned `61`, exact `0`, box `20`, VTRAC `51`.
- `brain1:dominant_canonicals`: pre-draw aligned `51`, exact `0`, box `9`, VTRAC `51`.
- `translation_sandbox:diagnostic_vt_box_seed`: pre-draw aligned `46`, exact `0`, box `0`, VTRAC `46`.
- `brain1:secondary_canonicals`: pre-draw aligned `43`, exact `0`, box `8`, VTRAC `43`.
- `positional:positional_canonical`: pre-draw aligned `39`, exact `0`, box `5`, VTRAC `39`.
- `positional:positional_combo`: pre-draw aligned `39`, exact `0`, box `5`, VTRAC `39`.
- `old_play_card:ranked_candidate_canonical`: pre-draw aligned `36`, exact `0`, box `17`, VTRAC `36`.
- `old_play_card:ranked_candidate_combo`: pre-draw aligned `36`, exact `3`, box `17`, VTRAC `36`.
- `blackapple:recommended_canonicals`: pre-draw aligned `35`, exact `0`, box `5`, VTRAC `35`.

## 5. Guardrails

- Do not build one master score yet; first add exposure/false-positive denominators for source keys.
- Keep Brain2 rank diagnostics active because static rank can make top-primary metrics look stronger than they are.
- Keep bonus/fireball sidecar separate from standard boxed/straight metrics.
- Use this audit to choose fixtures for future translator tests before rewriting candidate generation.
