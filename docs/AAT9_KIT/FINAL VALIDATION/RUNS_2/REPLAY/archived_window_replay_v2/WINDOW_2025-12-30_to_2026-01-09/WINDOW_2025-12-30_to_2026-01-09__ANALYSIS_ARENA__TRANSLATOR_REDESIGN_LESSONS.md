# Translator Redesign Lessons From Evidence Utilization Audit

This memo converts the March audit into design guidance for a future Analysis Arena-native candidate translator.

## 1. Main Finding

- The primary redesign target is not more broad evidence capture; it is cleaner promotion from evidence into separated boxed, straight, VTRAC, and decay lanes.
- Captured-and-used: `63`; captured-but-underused: `12`; wrong-lane: `51`.
- Box/exact gaps: `12`; VTRAC-only: `115`.

## 2. Candidate Lane Implications

- Boxed lane should prioritize exact/box-aligned Arena, sandbox, play-card, profit-alert, double-anchor, family-frontier, and box-gap evidence.
- Straight lane should remain stricter: exact sandbox, exact play-card, literal frontier, positional combo exactness, and direct profit-alert evidence should carry more weight than broad canonical context.
- VTRAC lane should be treated as territory/carryforward unless paired with box/exact evidence or a strong frontier/double signal.
- Decay lane should remain separate from same-day grading but feed carryforward watch decisions.

## 3. Signals Worth Promoting Into Future Scoring Experiments

- `play_card_any_box`: present `21`, converted `21`, gap `0`; Conversion-grade candidate signal in this window.
- `sandbox_exact_seed`: present `4`, converted `4`, gap `0`; Conversion-grade candidate signal in this window.
- `arena_exact_signal`: present `4`, converted `4`, gap `0`; Conversion-grade candidate signal in this window.
- `play_card_any_exact`: present `39`, converted `34`, gap `5`; Conversion-grade candidate signal in this window.
- `sandbox_box_seed`: present `19`, converted `10`, gap `9`; High-priority translator-learning signal; often saw value that old final layer missed.
- `arena_primary_box`: present `15`, converted `7`, gap `8`; High-priority translator-learning signal; often saw value that old final layer missed.
- `arena_box_signal`: present `22`, converted `10`, gap `12`; High-priority translator-learning signal; often saw value that old final layer missed.

## 4. Source Rows Worth Preserving For Brain1/Brain2 Training

- `old_candidate_universe:pack:stable_top`: pre-draw aligned `182`, exact `0`, box `24`, VTRAC `182`.
- `translation_sandbox:diagnostic_straight_seed`: pre-draw aligned `155`, exact `8`, box `19`, VTRAC `151`.
- `old_play_card:budgeted_canonicals_top`: pre-draw aligned `139`, exact `0`, box `21`, VTRAC `139`.
- `old_play_card:ranked_candidate_canonical`: pre-draw aligned `135`, exact `0`, box `27`, VTRAC `135`.
- `old_play_card:ranked_candidate_combo`: pre-draw aligned `135`, exact `7`, box `27`, VTRAC `135`.
- `translation_sandbox:diagnostic_boxed_seed`: pre-draw aligned `147`, exact `0`, box `38`, VTRAC `128`.
- `translation_sandbox:diagnostic_vt_box_seed`: pre-draw aligned `109`, exact `0`, box `0`, VTRAC `109`.
- `brain1:secondary_canonicals`: pre-draw aligned `106`, exact `0`, box `15`, VTRAC `106`.
- `old_candidate_universe:top_canonicals`: pre-draw aligned `101`, exact `0`, box `17`, VTRAC `101`.
- `brain1:dominant_canonicals`: pre-draw aligned `93`, exact `0`, box `15`, VTRAC `93`.
- `blackapple:recommended_canonicals`: pre-draw aligned `88`, exact `0`, box `15`, VTRAC `88`.
- `positional:positional_combo`: pre-draw aligned `82`, exact `1`, box `7`, VTRAC `82`.

## 5. Guardrails

- Do not build one master score yet; first add exposure/false-positive denominators for source keys.
- Keep Brain2 rank diagnostics active because static rank can make top-primary metrics look stronger than they are.
- Keep bonus/fireball sidecar separate from standard boxed/straight metrics.
- Use this audit to choose fixtures for future translator tests before rewriting candidate generation.
