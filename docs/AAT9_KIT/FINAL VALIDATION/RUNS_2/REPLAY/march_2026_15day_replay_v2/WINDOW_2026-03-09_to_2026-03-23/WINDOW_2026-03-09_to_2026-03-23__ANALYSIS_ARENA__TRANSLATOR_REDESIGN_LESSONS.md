# Translator Redesign Lessons From Evidence Utilization Audit

This memo converts the March audit into design guidance for a future Analysis Arena-native candidate translator.

## 1. Main Finding

- The primary redesign target is not more broad evidence capture; it is cleaner promotion from evidence into separated boxed, straight, VTRAC, and decay lanes.
- Captured-and-used: `97`; captured-but-underused: `23`; wrong-lane: `66`.
- Box/exact gaps: `23`; VTRAC-only: `141`.

## 2. Candidate Lane Implications

- Boxed lane should prioritize exact/box-aligned Arena, sandbox, play-card, profit-alert, double-anchor, family-frontier, and box-gap evidence.
- Straight lane should remain stricter: exact sandbox, exact play-card, literal frontier, positional combo exactness, and direct profit-alert evidence should carry more weight than broad canonical context.
- VTRAC lane should be treated as territory/carryforward unless paired with box/exact evidence or a strong frontier/double signal.
- Decay lane should remain separate from same-day grading but feed carryforward watch decisions.

## 3. Signals Worth Promoting Into Future Scoring Experiments

- `play_card_any_box`: present `29`, converted `29`, gap `0`; Conversion-grade candidate signal in this window.
- `play_card_any_exact`: present `54`, converted `51`, gap `3`; Conversion-grade candidate signal in this window.
- `sandbox_exact_seed`: present `9`, converted `7`, gap `2`; Conversion-grade candidate signal in this window.
- `arena_exact_signal`: present `9`, converted `7`, gap `2`; Conversion-grade candidate signal in this window.
- `sandbox_box_seed`: present `27`, converted `12`, gap `15`; High-priority translator-learning signal; often saw value that old final layer missed.
- `arena_box_signal`: present `35`, converted `14`, gap `21`; High-priority translator-learning signal; often saw value that old final layer missed.
- `arena_primary_box`: present `25`, converted `9`, gap `16`; High-priority translator-learning signal; often saw value that old final layer missed.

## 4. Source Rows Worth Preserving For Brain1/Brain2 Training

- `old_candidate_universe:pack:stable_top`: pre-draw aligned `285`, exact `0`, box `38`, VTRAC `285`.
- `translation_sandbox:diagnostic_straight_seed`: pre-draw aligned `255`, exact `18`, box `30`, VTRAC `246`.
- `translation_sandbox:diagnostic_boxed_seed`: pre-draw aligned `243`, exact `0`, box `54`, VTRAC `216`.
- `old_play_card:ranked_candidate_canonical`: pre-draw aligned `209`, exact `0`, box `23`, VTRAC `209`.
- `old_play_card:ranked_candidate_combo`: pre-draw aligned `209`, exact `7`, box `23`, VTRAC `209`.
- `old_play_card:budgeted_canonicals_top`: pre-draw aligned `208`, exact `0`, box `29`, VTRAC `208`.
- `brain1:secondary_canonicals`: pre-draw aligned `191`, exact `0`, box `22`, VTRAC `191`.
- `brain1:dominant_canonicals`: pre-draw aligned `172`, exact `0`, box `25`, VTRAC `172`.
- `translation_sandbox:diagnostic_vt_box_seed`: pre-draw aligned `162`, exact `0`, box `0`, VTRAC `162`.
- `old_candidate_universe:top_canonicals`: pre-draw aligned `150`, exact `0`, box `18`, VTRAC `150`.
- `blackapple:recommended_canonicals`: pre-draw aligned `133`, exact `0`, box `17`, VTRAC `133`.
- `positional:positional_combo`: pre-draw aligned `116`, exact `6`, box `18`, VTRAC `116`.

## 5. Guardrails

- Do not build one master score yet; first add exposure/false-positive denominators for source keys.
- Keep Brain2 rank diagnostics active because static rank can make top-primary metrics look stronger than they are.
- Keep bonus/fireball sidecar separate from standard boxed/straight metrics.
- Use this audit to choose fixtures for future translator tests before rewriting candidate generation.
