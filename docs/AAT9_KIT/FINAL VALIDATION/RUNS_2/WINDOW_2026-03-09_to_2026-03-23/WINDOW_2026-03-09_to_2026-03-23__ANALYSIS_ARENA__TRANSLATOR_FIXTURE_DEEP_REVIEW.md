# Translator Fixture Deep Review

Purpose: convert Stage 1 and Stage 2 evidence into stable translator teaching sets.

## Fixture Counts

- Priority fixture rows: `67`
- Gap teacher stack rows: `270`
- Positive regression fixtures: `97`
- Decay carryforward fixtures: `103`

Evidence status mix:
- `CAPTURED_BUT_NOT_PROMOTED`: `125`
- `DECAY_VALIDATED`: `103`
- `CAPTURED_AND_USED`: `97`
- `CAPTURED_BUT_WRONG_LANE`: `66`
- `CAPTURED_BUT_UNDERUSED`: `23`

Outcome mix:
- `VTRAC_ONLY`: `141`
- `NO_CONVERSION`: `138`
- `BOX_ANY`: `61`
- `STRAIGHT`: `51`
- `BOX_GAP`: `21`
- `EXACT_GAP`: `2`

## Fixture Use

- Gap teachers show where evidence existed but the old downstream layer under-expressed it.
- Wrong-lane cases define restraint rules, especially for VTRAC territory.
- Positive conversions become regression anchors for future translator edits.
- Decay cases preserve the carryforward/watch concept without contaminating same-day scoring.
