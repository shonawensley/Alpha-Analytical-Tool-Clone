# Translator Fixture Deep Review

Purpose: convert Stage 1 and Stage 2 evidence into stable translator teaching sets.

## Fixture Counts

- Priority fixture rows: `46`
- Gap teacher stack rows: `18`
- Positive regression fixtures: `23`
- Decay carryforward fixtures: `19`

Evidence status mix:
- `CAPTURED_BUT_NOT_PROMOTED`: `25`
- `CAPTURED_AND_USED`: `23`
- `DECAY_VALIDATED`: `19`
- `CAPTURED_BUT_WRONG_LANE`: `15`
- `CAPTURED_BUT_UNDERUSED`: `2`

Outcome mix:
- `VTRAC_ONLY`: `35`
- `NO_CONVERSION`: `21`
- `BOX_ANY`: `14`
- `STRAIGHT`: `12`
- `BOX_GAP`: `2`

## Fixture Use

- Gap teachers show where evidence existed but the old downstream layer under-expressed it.
- Wrong-lane cases define restraint rules, especially for VTRAC territory.
- Positive conversions become regression anchors for future translator edits.
- Decay cases preserve the carryforward/watch concept without contaminating same-day scoring.
