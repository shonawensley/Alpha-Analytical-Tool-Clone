# Translator Fixture Deep Review

Purpose: convert Stage 1 and Stage 2 evidence into stable translator teaching sets.

## Fixture Counts

- Priority fixture rows: `48`
- Gap teacher stack rows: `42`
- Positive regression fixtures: `30`
- Decay carryforward fixtures: `30`

Evidence status mix:
- `CAPTURED_AND_USED`: `30`
- `DECAY_VALIDATED`: `30`
- `CAPTURED_BUT_NOT_PROMOTED`: `23`
- `CAPTURED_BUT_WRONG_LANE`: `22`
- `CAPTURED_BUT_UNDERUSED`: `4`

Outcome mix:
- `VTRAC_ONLY`: `42`
- `NO_CONVERSION`: `30`
- `BOX_ANY`: `18`
- `STRAIGHT`: `15`
- `BOX_GAP`: `4`

## Fixture Use

- Gap teachers show where evidence existed but the old downstream layer under-expressed it.
- Wrong-lane cases define restraint rules, especially for VTRAC territory.
- Positive conversions become regression anchors for future translator edits.
- Decay cases preserve the carryforward/watch concept without contaminating same-day scoring.
