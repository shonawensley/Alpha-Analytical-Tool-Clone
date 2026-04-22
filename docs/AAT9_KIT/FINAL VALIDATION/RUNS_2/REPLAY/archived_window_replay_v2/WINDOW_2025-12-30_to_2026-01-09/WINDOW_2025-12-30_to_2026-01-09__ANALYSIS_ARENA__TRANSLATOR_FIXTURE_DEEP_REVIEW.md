# Translator Fixture Deep Review

Purpose: convert Stage 1 and Stage 2 evidence into stable translator teaching sets.

## Fixture Counts

- Priority fixture rows: `56`
- Gap teacher stack rows: `135`
- Positive regression fixtures: `63`
- Decay carryforward fixtures: `94`

Evidence status mix:
- `DECAY_VALIDATED`: `94`
- `CAPTURED_BUT_NOT_PROMOTED`: `81`
- `CAPTURED_AND_USED`: `63`
- `CAPTURED_BUT_WRONG_LANE`: `51`
- `CAPTURED_BUT_UNDERUSED`: `12`

Outcome mix:
- `VTRAC_ONLY`: `115`
- `NO_CONVERSION`: `100`
- `BOX_ANY`: `40`
- `STRAIGHT`: `34`
- `BOX_GAP`: `12`

## Fixture Use

- Gap teachers show where evidence existed but the old downstream layer under-expressed it.
- Wrong-lane cases define restraint rules, especially for VTRAC territory.
- Positive conversions become regression anchors for future translator edits.
- Decay cases preserve the carryforward/watch concept without contaminating same-day scoring.
